from django.shortcuts import render, redirect

from .forms import LoginForm ,UserPasswordResetForm,RegisterForm,SignupForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from .tokens import account_activation_token

from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.utils.encoding import force_bytes,force_str
# Create your views here.
def logIn(request, *args, **kwargs):
    login_form = LoginForm(request.POST or None)
    pass_form = UserPasswordResetForm(request.POST or None)
    if login_form.is_valid():
        
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        get_user_email = User.objects.filter(email=email).first()

        if get_user_email is not None:
            user = authenticate(request, username=get_user_email, password=password)
        else:
            user = None
            
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
    
    username = request.user.username

    context = {
        'username' : username,
        # 'setting': site_setting,
        'login_form': login_form
    }
    return render(request, 'logIn.html', context)


def createAccount(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    
    register_form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('user_name')
            password = register_form.cleaned_data.get('password')
            email = register_form.cleaned_data.get('email')
            # re_password = register_form.cleaned_data.get('re_password')
            captcha =register_form.cleaned_data.get('captcha')
            print(f"user_name={user_name}")
            print(f"password={password}")
            print(f"email={email}")
            # print(f"captcha={captcha}")

            user = User.objects.create_user(username=user_name,email=email,password=password,is_active = False)
            print(user.pk)

            current_site = get_current_site(request)

            mail_subject = 'فعال سازی اکانت'
            message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                    
                })
            to_email = register_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        # ! bar roy zaher in ghesmat kar shavad
            return HttpResponse("لینک فعال سازی یه ایمیل شما ارسال شد <a href='/account/logIn/'>")

    context = {
        'register_form': register_form,
    }
    return render(request, 'createAccount.html', context)

def log_out(request):
    logout(request)
    return redirect('/new_account/logIn/')

def activate(request, uidb64, token):
    try:
        # uid = force_text(urlsafe_base64_decode(uidb64))
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        #! front bishtar kar shavad
        return HttpResponse('اکانت شما با موفقیت فعال شد. برای <a href="/login"> ورود </a>')
    else:
        return HttpResponse('لینک فعال سازی منقضی شده است!<a href="/register"> دوباره امتحان کنید </a>')
