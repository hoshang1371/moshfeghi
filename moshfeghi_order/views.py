from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Product.models import Product
from moshfeghi_order.forms import UserNewOrderForm
from moshfeghi_order.models import Order
from django.contrib import messages

@login_required(login_url='/login')
def add_user_order(request):
    # print("hojjat")
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(
            owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        if( count > int(product.number)):
            messages.warning(request, 'این تعداد کالا در انبار موجود نمی باشد.')
            return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')
        # TODO if order is exsist
        x = order.orderdetail_set.filter(product_id=product.id)
        #* agar kala dar sabad kharid mojod bood
        if x:
            messages.warning(request, 'این کالا در سبد خرید موجوداست.')
            return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')
        else :
            order.orderdetail_set.create(product_id=product.id, price=product.price ,count=count)
        # todo: redirect user to user panel
        messages.success(request, "محصول مورد نظر به سبد خرید اضافه شد.")       
        # return redirect('/products')
        return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')

    return redirect('/')
