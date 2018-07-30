from django.conf.urls import url, include

from app import forms
from app.views import account, auth, general, order
from app.views.crud import AccountCrudView, CrudView


def crud(view, title):
    return url(r'^{}/'.format(title), include([
        url(r'^$', view.index, name="index"),
        url(r'^add/', view.add, name="add"),
        url(r'^edit/(?P<pk>[0-9]+)', view.edit, name="edit"),
        url(r'^remove/(?P<pk>[0-9]+)', view.remove, name="remove"),
    ], namespace=title))

urlpatterns = [
    url(r'^$', general.index, name="index"),

    url(r'^account/', include([
        url(r'^edit/', account.edit, name="edit"),
    ], namespace='account')),

    url(r'^auth/', include([
        url(r'^login/', auth.login, name="login"),
        url(r'^logout/', auth.login, name="logout"),
        url(r'^sign/', auth.sign, name="sign"),
    ], namespace='auth')),

    crud(CrudView(forms.CityForm), "city"),
    crud(CrudView(forms.CountryForm), "country"),
    crud(CrudView(forms.CurrencyForm), "currency"),
    crud(CrudView(forms.PlaceForm, user_specific=True), "place"),
    crud(CrudView(forms.PlaceTypeForm), "placetype"),
    crud(CrudView(forms.TariffForm), "tariff"),

    crud(AccountCrudView(forms.ClientForm), "client"),
    crud(AccountCrudView(forms.ManagerForm), "manager"),
    crud(AccountCrudView(forms.PartnerForm), "partner"),

    url(r'^order/', include([
        url(r'^client/', order.by_client, name="client"),
        url(r'^partner/', order.by_partner, name="partner"),
        url(r'^place/(?P<pk>[0-9]+)', order.place, name="place"),
        url(r'^edit/(?P<pk>[0-9]+)', order.discard, name="edit"),
        url(r'^discard/(?P<pk>[0-9]+)', order.discard, name="discard"),
    ], namespace='order')),

    url(r'^', general.error),
]
