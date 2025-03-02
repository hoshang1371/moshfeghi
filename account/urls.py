from django.urls import path

from .views import logIn,createAccount,log_out

urlpatterns = [
    path('logIn/', logIn, name="logIn"),
    path('createAccount/', createAccount, name='createAccount'),
    path('log_out/', log_out, name='log_out'),
]