from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Product.models import Product
from moshfeghi_order.forms import UserNewOrderForm
from moshfeghi_order.models import Order
from django.contrib import messages

from moshfeghi_order.serializer import DeleteOrderDetailSerializer
from .models import Order,OrderDetail
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView, 
    # RetrieveAPIView, 
    # RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

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


class DeleteOrderDetail(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = DeleteOrderDetailSerializer
    permission_classes = [IsAuthenticated]

@login_required(login_url='/login')
def List_user_open_order(request):
    # print("kir khar")
    # logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    # post_price = PostPrice.objects.filter().first()
    # print("post_price=",post_price.price)
    # print(order_partials_buy)
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    username = request.user.username
    # site_setting = SiteSetting.objects.first()

    contex = {
        'username' : username,
        'order_partials_buy': order_partials_buy,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        # 'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
    }
    return render(request ,'list_of_buy.html',contex)