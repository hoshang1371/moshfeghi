from django.shortcuts import render


# Create your views here.
def logIn(request, *args, **kwargs):

    context = {

    }
    return render(request, 'logIn.html', context)

