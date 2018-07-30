from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Place, Client


@login_required(login_url="/login")
def index(request):
    if request.user.role.name == "client":
        client = Client.objects.get(user=request.user)
        return render(request, "general/index_client.html", {
            "places": client.city.places.all()
        })
    else:
        return render(request, "general/index.html", {})


def error(request):
    return render(request, "general/error.html", {})
