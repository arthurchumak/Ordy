from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import UserForm, ClientForm, PartnerForm, PasswordForm
from app.models import Client, Partner


@login_required()
def edit(request):

    forms = []

    if request.user.role.name == "client":
        client = Client.objects.get(user=request.user)
        forms.append(ClientForm(request.POST or None, instance=client))
    elif request.user.role.name == "partner":
        partner = Partner.objects.get(user=request.user)
        forms.append(PartnerForm(request.POST or None, instance=partner))

    user_form = UserForm(request.POST or None, instance=request.user)

    forms += [user_form, PasswordForm]

    if request.method == "GET":
        return render(request, "shared/editor.html", {
            "forms": forms,
            "index_link": reverse("index")
        })
    elif request.method == "POST":
        password_form = PasswordForm(request.POST)

        additional = True

        if request.user.role.name == "client":
            client = Client.objects.get(user=request.user)
            form = ClientForm(request.POST or None, instance=client)
            forms.append(form)
            additional = form.is_valid()
        elif request.user.role.name == "partner":
            partner = Partner.objects.get(user=request.user)
            form = PartnerForm(request.POST or None, instance=partner)
            forms.append(form)
            additional = form.is_valid()

        if user_form.is_valid() and password_form.is_valid() and additional:
            if request.user.role.name in ("client", "partner"):
                form.save()
            user = user_form.save(commit=False)
            password = password_form.cleaned_data.get("password")
            if password and not user.check_password(password):
                user.set_password(password)
                user.save()
                return redirect("auth:logout")
            user.save()
            return redirect("index")
        else:
            return render(request, "shared/editor.html", {
                "forms": forms,
                "index_link": reverse("index")
            })
