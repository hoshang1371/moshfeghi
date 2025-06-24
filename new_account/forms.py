from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()
from django.core import validators
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField, CaptchaTextInput

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

CHOICES = [('1', 'اقا'), ('2', 'خانم')]
SAL = (())
MAH = (
        ('فروردین' , 'فروردین'),
        ('اریبهشت' , 'اریبهشت'),
        ('خرداد' , 'خرداد'),
        ('تیر' , 'تیر'),
        ('مرداد' , 'مرداد'),
        ('شهریور' , 'شهریور'),
        ('مهر' , 'مهر'),
        ('آبان' , 'آبان'),
        ('آذر' , 'آذر'),
        ('دی' , 'دی'),
        ('بهمن' , 'بهمن'),
        ('اسفند' , 'اسفند'),
    )
ROZ = (())

for i in range(1300,1500):
    SAL = SAL + ((f'{i}',f'{i}'),)

for j in range(1,31):
    ROZ = ROZ + ((f'{j}',f'{j}'),)

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={ 'type':"email",'value':"",'class':'form-control ','id':"customer_email",'size':"30"}),
        label=' نام کاربری '
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class':'form-control'}),
        label=' کلمه ی عبور '
    )


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



class EditUserForm(forms.Form):

    first_name= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام  خود را وارد نمایید ', 'class' : 'form-control rtl'}),
        label=' نام  '
    )

    last_name= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام خانوادگی خود را وارد نمایید ', 'class' : 'form-control rtl'}),
        label=' نام خانوادگی '
    )

    choice_field = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=CHOICES,
        label=' عنوان اجتماعی '
        )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ایمیل',"class":"form-control rtl"}),
        label=' ایمیل',
        validators=[
            validators.EmailValidator(' ایمیل وارد شده معتبر نمی باشد ')
        ]
    )

    SAL = forms.ChoiceField(
        choices=SAL,
        widget=forms.Select(attrs={"class":"form-control rtl me-2"}),
        )

    MAH = forms.ChoiceField(
        choices=MAH,
        widget=forms.Select(attrs={"class":"form-control rtl me-2"}),
        )

    ROZ = forms.ChoiceField(
        choices=ROZ,
        widget=forms.Select(attrs={"class":"form-control rtl me-2"}),
        )

class ChangePass(forms.Form):
    password_now = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'گذرواژه فعلی',"class":"form-control rtl password"}),
        label=' گذرواژه فعلی',
    )

    password_new = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' رمز عبور جدید',"class":"form-control rtl password"}),
        label=' رمز عبور جدید ',
    )

    # password_accept = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder':' تاییدیه ',"class":"rtl"}),
    #     label=' تاییدیه ',
    #     validators=[
    #         validators.EmailValidator(' تاییدیه ')
    #     ]
    # )

    password_accept = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' تکرار رمز عبور جدید',"class":"form-control rtl password"}),
        label=' رمز عبور جدید ',
    )

    def clean_password_accept(self):
        password_new = self.cleaned_data.get('password_new')
        password_accept = self.cleaned_data.get('password_accept')

        if password_new != password_accept:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')
        elif (len(password_new) < 4):
            raise forms.ValidationError('کلمه های عبور باید بیشتر از چهار حرف باشد  ')


        return password_new

