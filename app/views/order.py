import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.models import Client, Place, Order, Partner
from app.forms import OrderForm


sidebar = "order"


@login_required()
def place(request, pk):
    place = Place.objects.get(id=pk)
    form = OrderForm(request.POST or None)

    if request.method == "GET":
        return render(request, "order/place.html", {
            "sidebar": sidebar,
            "place": place,
            "form": form
        })
    elif request.method == "POST":
        if form.is_valid():
            order = form.save(commit=False)
            order.client = Client.objects.get(user=request.user)
            order.place = place
            order.datetime = datetime.datetime.now()
            order.save()
            return redirect("index")
        else:
            return render(request, "order/place.html", {
                "sidebar": sidebar,
                "place": place,
                "form": form
            })


@login_required()
def discard(request, pk):
    pass



@login_required()
def by_client(request):
    return render(request, "order/table.html", {
        "sidebar": sidebar,
        "fields": Order.table_columns(),
        "list": Client.objects.get(user=request.user).orders.all()
    })


@login_required()
def by_partner(request):
    return render(request, "order/table.html", {
        "sidebar": sidebar,
        "fields": Order.table_columns(),
        "list": Order.objects.filter(place__partner__user=request.user)
    })
