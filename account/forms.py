from django import forms



class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={ 'type':"email",'value':"",'class':'form-control ','id':"customer_email",'size':"30"}),
        label=' نام کاربری '
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class':'form-control'}),
        label=' کلمه ی عبور '
    )


from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        "class":"rtl form-control",'type':"email",'value':"",'size':"30",'id':"recover-email","name":"email"
        }))
    
class UserSetPasswordForm(SetPasswordForm):
    # def __init__(self, *args, **kwargs):
    #     super(SetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "tabindex":"2"
        }))

    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "tabindex":"2"
        }))
