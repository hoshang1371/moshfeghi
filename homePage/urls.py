from django.urls import path
from homePage import views

urlpatterns = [
    path('', views.index, name='index')
]