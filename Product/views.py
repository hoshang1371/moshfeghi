from django.shortcuts import render

# Create your views here.
def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product_name = kwargs['name']
    print(selected_product_id,product_name)
    context = {

    }   


    return render(request, 'product_detail.html', context)