from django import forms

from app import models


class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = ('country', 'name')


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ('city', 'name', 'phone')


class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = ('name', 'code', 'currency')


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = ('code', 'coins')


class ManagerForm(forms.ModelForm):
    class Meta:
        model = models.Manager
        fields = ('country',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('persons', 'wish')


class PartnerForm(forms.ModelForm):
    class Meta:
        model = models.Partner
        fields = ('country', 'tariff', 'title',)


class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ('type', 'city', 'address', 'name', 'phone', 'open_time', 'close_time', 'capacity')


class PlaceTypeForm(forms.ModelForm):
    class Meta:
        model = models.PlaceType
        fields = ('name',)


class TariffForm(forms.ModelForm):
    class Meta:
        model = models.Tariff
        fields = ('country', 'name', 'description', 'price', 'places_limit', 'advertising')


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'email')


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=12)
