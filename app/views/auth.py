from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, "login.html", {
                "form": request.POST,
                "error": "Invalid credentials"
            })


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
