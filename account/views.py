from django.shortcuts import render, redirect

from .forms import LoginForm
from django.contrib.auth import login, get_user_model, authenticate, logout

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def logIn(request, *args, **kwargs):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        print("email:",email)
        print("password:",password)
        get_user_email = User.objects.get(email=email)
        user = authenticate(request, username=get_user_email, password=password)

        # print(user_name)
        # print(password)
        print(user)
        print(get_user_email)
        # print(login_form.cleaned_data)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
    
    username = request.user.username

    context = {
        'username' : username,
        # 'setting': site_setting,
        'login_form': login_form
    }
    return render(request, 'logIn.html', context)


def createAccount(request, *args, **kwargs):

    context = {

    }
    return render(request, 'createAccount.html', context)

def log_out(request):
    logout(request)
    return redirect('/account/logIn/')