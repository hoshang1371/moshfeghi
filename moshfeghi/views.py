from django.shortcuts import render, redirect
from Product.models import Product
from moshfeghi_slider.models import Slider,SliderDown

def home_page(request):
    # vige_products = Product.objects.order_by('-vige').all()[:10]
    # TODO:sliders
    sliders = Slider.objects.all()
    sliders_down = SliderDown.objects.all()

    most_visit_product = Product.objects.order_by('-visit_count').all()[:15]
    latest_products = Product.objects.order_by('-id').all()[:10]
    vige_products = Product.objects.filter(vige=True).all()[:10]
    print(f"sliders={sliders}")

    context ={
        'sliders_down':sliders_down,
        'sliders' : sliders,
        'most_visit_s' : most_visit_product,
        'latest_products' : latest_products,
        'vige_products' : vige_products,
    }
    return render(request, 'homePage.html', context )


def about_page_header(request):
    return render(request, 'shared/_HeaderRefrences.html')