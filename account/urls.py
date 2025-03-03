from django.urls import path

from django.contrib.auth import views

from .views import logIn,createAccount,log_out

from .forms import UserPasswordResetForm, UserSetPasswordForm

urlpatterns = [
    path('logIn/', logIn, name="logIn"),
    path('createAccount/', createAccount, name='createAccount'),
    path('log_out/', log_out, name='log_out'),
]

urlpatterns += [

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(
                    template_name='password_reset_form.html',
                    form_class=UserPasswordResetForm,
                    ), 
        name='password_reset'
        ),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
                    template_name='password_reset_confirm.html',
                    form_class = UserSetPasswordForm
                    ), 
        name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]