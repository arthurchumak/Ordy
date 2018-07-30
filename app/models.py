from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Currency(models.Model):
    code = models.CharField(max_length=3)
    coins = models.BooleanField()

    def __str__(self):
        return self.code

    @staticmethod
    def table_columns():
        return ["Code", "Has coins"]

    def table_values(self):
        return [self.code, "Yes" if self.coins else "No"]

    def format_value(self, value):
        return "{} {}".format(
            round(value*100)/100 if self.coins else round(value),
            self.code
        )


class Country(models.Model):
    currency = models.ForeignKey(Currency, related_name="countries")

    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    @staticmethod
    def table_columns():
        return ["Name", "Currency"]

    def table_values(self):
        return [self.name, self.currency]


class City(models.Model):
    country = models.ForeignKey(Country, related_name="cities")
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @staticmethod
    def table_columns():
        return ["Country", "Name"]

    def table_values(self):
        return [self.country, self.name]


class Tariff(models.Model):
    country = models.ForeignKey(Country, related_name="tariffs")
    is_active = models.BooleanField(default=True)

    description = models.CharField(max_length=50)
    name = models.CharField(max_length=30)

    price = models.FloatField()

    places_limit = models.PositiveIntegerField()
    advertising = models.BooleanField()

    def __str__(self):
        return f"{self.country} - {self.name} - {self.price_formatted()}"

    @staticmethod
    def table_columns():
        return ["Country", "Name", "Price", "Places limit", "AD"]

    def table_values(self):
        return [self.country, self.name, self.country.currency.format_value(self.price), self.places_limit, "Yes" if self.advertising else "No"]

    def price_formatted(self):
        return self.country.currency.format_value(self.price)


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, related_name="users")

    def __str__(self):
        return self.username

    @staticmethod
    def table_columns():
        return ["Username", "Email"]

    def table_values(self):
        return [self.username, self.email]


class Manager(models.Model):
    user = models.ForeignKey(User)
    country = models.ForeignKey(Country, related_name="managers")

    def __str__(self):
        return self.user.username

    @staticmethod
    def table_columns():
        return ["Country", "Username"]

    def table_values(self):
        return [self.country, self.user.username]


class Partner(models.Model):
    user = models.ForeignKey(User)
    country = models.ForeignKey(Country, related_name="partners")
    tariff = models.ForeignKey(Tariff, related_name="partners")

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    @staticmethod
    def table_columns():
        return ["Country", "Title"]

    def table_values(self):
        return [self.country, self.title]


class Client(models.Model):
    user = models.ForeignKey(User)
    city = models.ForeignKey(City, related_name="clients")

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def table_columns():
        return ["City", "Username", "Phone"]

    def table_values(self):
        return [self.city, self.user.username, self.phone]


class PlaceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def table_columns():
        return ["Name"]

    def table_values(self):
        return [self.name]


class Place(models.Model):
    partner = models.ForeignKey(Partner, related_name="places")
    type = models.ForeignKey(PlaceType, related_name="places")
    city = models.ForeignKey(City, related_name="places")

    name = models.CharField(max_length=50)

    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)

    open_time = models.TimeField()
    close_time = models.TimeField()

    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.name} {self.address}"

    @staticmethod
    def table_columns():
        return ["Type", "Name", "Address"]

    def table_values(self):
        return [self.type, self.name, self.address]

    def random_photo(self):
        try:
            return self.photos.order_by('?').first().image.url
        except:
            return ""

    @classmethod
    def get_list(cls, user):
        if user.role.name == "partner":
            partner = Partner.objects.get(user=user)
            return partner.places.all()
        else:
            return cls.objects.all()

    @classmethod
    def form_save(cls, form, user):
        partner = Partner.objects.get(user=user)
        place = form.save(commit=False)
        place.partner = partner
        place.save()


class PlacePhoto(models.Model):
    place = models.ForeignKey(Place, related_name="photos")
    image = models.ImageField()


class Order(models.Model):
    client = models.ForeignKey(Client, related_name="orders")
    place = models.ForeignKey(Place, related_name="orders")

    active = models.BooleanField(default=True)

    persons = models.IntegerField()
    datetime = models.DateTimeField()
    wish = models.CharField(max_length=300)

    @staticmethod
    def table_columns():
        return ["Phone", "Place", "Time", "Persons", "Message"]

    def table_values(self):
        return [self.client.phone, self.place, self.datetime, self.persons, self.wish]

    def edit_link(self):
        return reverse("order:edit", args=[self.id])

    def discard_link(self):
        return reverse("order:discard", args=[self.id])


class Review(models.Model):
    order = models.ForeignKey(Order)

    datetime = models.DateTimeField()

    text = models.CharField(max_length=300)
    recommendation = models.BooleanField()


class RequestType(models.Model):
    role = models.ForeignKey(Role)

    name = models.CharField(max_length=50)


class Request(models.Model):
    type = models.ForeignKey(RequestType, related_name="requests")

    text = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
