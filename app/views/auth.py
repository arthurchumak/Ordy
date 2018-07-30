from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.models import User, Role

role = Role.objects.get_or_create(name="client")[0]


def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, "auth/login.html", {
                "form": request.POST,
                "error": "Invalid credentials"
            })


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('auth:login')

role = Role

def sign(request):
    if request.method == "GET":
        return render(request, "auth/sign.html")
    elif request.method == "POST":
        try:
            User.create_with_role(
                username=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
                role=role
            ).save()
            return render(request, "auth/login.html", {
                "form": request.POST
            })
        except:
            return render(request, "auth/sign.html", {
                "form": request.POST,
                "error": "Username exists"
            })
