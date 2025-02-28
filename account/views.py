from django.shortcuts import render


# Create your views here.
def logIn(request, *args, **kwargs):

    context = {

    }
    return render(request, 'logIn.html', context)


def logOut(request, *args, **kwargs):

    context = {

    }
    return render(request, 'logOut.html', context)

