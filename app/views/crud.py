from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import PasswordForm, UserForm
from app.models import Role


class CrudView(object):
    def __init__(self, form, user_specific=False):
        self.Form = form
        self.Model = form.Meta.model

        self.name = self.Model.__name__.lower()

        self.Model.list_link = lambda: reverse(f"{self.name}:index")
        self.Model.add_link = lambda: reverse(f"{self.name}:add")
        self.Model.edit_link = lambda obj: reverse(f"{self.name}:edit", args=[obj.id])
        self.Model.remove_link = lambda obj: reverse(f"{self.name}:remove", args=[obj.id])

        self.user_specific = user_specific

    def index(self, request):
        return render(request, "shared/table.html", {
            "sidebar": self.name,
            "list": self.Model.get_list(request.user) if self.user_specific else self.Model.objects.all(),
            "fields": self.Model.table_columns(),
            "add_link": self.Model.add_link()
        })

    def add(self, request):
        if request.method == "GET":
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [self.Form],
                "index_link": self.Model.list_link(),
            })
        elif request.method == "POST":
            form = self.Form(request.POST)
            if form.is_valid():
                if self.user_specific:
                    self.Model.form_save(form, request.user)
                else:
                    form.save()
                return redirect(self.Model.list_link())
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [form],
                "index_link": self.Model.list_link()
            })

    def edit(self, request, pk):
        obj = self.Model.objects.get(id=pk)
        form = self.Form(request.POST or None, instance=obj)

        if request.method == "GET":
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [form],
                "index_link": self.Model.list_link()
            })
        elif request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(self.Model.list_link())
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [form],
                "index_link": self.Model.list_link()
            })

    def remove(self, request, pk):
        obj = self.Model.objects.get(id=pk)
        if request.method == "GET":
            return render(request, "shared/remove.html", {
                "sidebar": self.name,
                "name": obj.__str__(),
                "form_action": obj.remove_link()
            })
        elif request.method == "POST":
            obj.delete()
            return redirect(self.Model.list_link())


class AccountCrudView(object):
    def __init__(self, form):
        self.Form = form
        self.Model = form.Meta.model
        self.name = self.Model.__name__.lower()

        self.role = Role.objects.get_or_create(name=self.name)[0]

        self.Model.list_link = lambda: reverse(f"{self.name}:index")
        self.Model.add_link = lambda: reverse(f"{self.name}:add")
        self.Model.edit_link = lambda obj: reverse(f"{self.name}:edit", args=[obj.id])
        self.Model.remove_link = lambda obj: reverse(f"{self.name}:remove", args=[obj.id])

    def index(self, request):
        return render(request, "shared/table.html", {
            "sidebar": self.name,
            "list": self.Model.objects.all(),
            "fields": self.Model.table_columns(),
            "add_link": self.Model.add_link()
        })

    def add(self, request):
        forms = [self.Form, UserForm, PasswordForm]
        if request.method == "GET":
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": forms,
                "index_link": self.Model.list_link(),
            })
        elif request.method == "POST":
            user_form = UserForm(request.POST)
            password_form = PasswordForm(request.POST)
            form = self.Form(request.POST)
            if user_form.is_valid() and password_form.is_valid() and form.is_valid():
                user, account = user_form.save(commit=False), form.save(commit=False)
                user.role = self.role
                user.set_password(password_form.cleaned_data.get("password"))
                user.save()
                account.user = user
                account.save()
                return redirect(self.Model.list_link())
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "form": [form, user_form, password_form],
                "index_link": self.Model.list_link()
            })

    def edit(self, request, pk):
        obj = self.Model.objects.get(id=pk)
        form = self.Form(request.POST or None, instance=obj)

        user_form = UserForm(request.POST or None, instance=obj.user)

        if request.method == "GET":
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [form, user_form, PasswordForm],
                "index_link": self.Model.list_link()
            })
        elif request.method == "POST":
            password_form = PasswordForm(request.POST or None)
            if user_form.is_valid() and form.is_valid() and password_form.is_valid():
                user, partner = user_form.save(commit=False), form.save(commit=False)
                user.set_password(password_form.cleaned_data.get("password"))
                user.save()
                form.user = user
                form.save()
                return redirect(self.Model.list_link())
            return render(request, "shared/editor.html", {
                "sidebar": self.name,
                "forms": [form, user_form, PasswordForm],
                "index_link": self.Model.list_link()
            })

    def remove(self, request, pk):
        obj = self.Model.objects.get(id=pk)
        if request.method == "GET":
            return render(request, "shared/remove.html", {
                "sidebar": self.name,
                "name": obj.__str__(),
                "form_action": obj.remove_link()
            })
        elif request.method == "POST":
            obj.user.is_active = False
            obj.user.save()
            obj.delete()
            return redirect(self.Model.list_link())
