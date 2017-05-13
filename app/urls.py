from django.conf.urls import url

from app.views import general, auth

urlpatterns = [
    url(r'^$', general.index, name="index"),
    url(r'^login', auth.login, name="login"),
    url(r'^logout', auth.login, name="logout"),
    url(r'^', general.error),
]
