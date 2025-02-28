from django.urls import path

from .views import logIn,logOut

urlpatterns = [
    path('logIn/', logIn),
    path('logOut/', logOut),
]