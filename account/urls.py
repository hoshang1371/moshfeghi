from django.urls import path

from .views import logIn

urlpatterns = [
    path('logIn/', logIn),
]