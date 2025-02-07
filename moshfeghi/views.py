from django.shortcuts import render, redirect

def home_page(request):

    return render(request, 'homePage.html' )


def about_page_header(request):
    return render(request, 'shared/_HeaderRefrences.html')