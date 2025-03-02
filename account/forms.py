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
