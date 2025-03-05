from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()
from django.core import validators
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField, CaptchaTextInput

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
    
# class CustomCaptchaTextInput(CaptchaTextInput):
#     template_name = 'custom_field.html'
    # template_name = 'captcha/captcha_field.html'
    # def __init__(self, *arg,**kwargs):
    #     super.__init__(self, *arg,**kwargs)
    #     for field in self.widgets:
    #  

class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","tabindex":"1"}),
        label=' نام کاربری ',
        # validators=[
        #     validators.MaxLengthValidator(limit_value=20,
        #                                  message='تعداد کارکتر های وارد شده نمی تواند بیشتر از 20 باشد'),
        #     validators.MinLengthValidator(4, 'تعداد کارکتر های وارد شده نمی تواند کمتر از 4 باشد')
        # ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","tabindex":"2","type":"email"}),
        label=' ایمیل',
        validators=[
            validators.EmailValidator(' ایمیل وارد شده معتبر نمی باشد ')
        ]
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={"class":"form-control password","tabindex":"3","type":"password"}),
        label=' کلمه ی عبور '
    )

    re_password = forms.CharField(
        widget= forms.PasswordInput(attrs={"class":"form-control password","tabindex":"4","type":"password"}),
        label=' تکرار کلمه ی عبور  '
    )
    #ToDO
    # captcha = CaptchaField(
    #     widget=CustomCaptchaTextInput
    # )
    captcha = CaptchaField(
        
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        
        if is_exists_user_by_email:
            raise forms.ValidationError(' ایمیل وارد شده تکراری می باشد ')

        # if len(email) > 20:
        #     raise forms.ValidationError(' تعداد کارکتر های وارد شده باید کمتر از 20 باشد ')

        return email
    
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلاً ثبت نام کرده است')

        return user_name


    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password
    

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
