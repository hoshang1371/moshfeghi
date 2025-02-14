from django.urls import path

from .views import product_detail

urlpatterns = [
    path('<productId>/<name>', product_detail),
]