from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Product.models import Product
from moshfeghi_order.forms import UserNewOrderForm
from moshfeghi_order.models import Order
from django.contrib import messages

from moshfeghi_order.serializer import DeleteOrderDetailSerializer, OrderProductDeleteListOfBuySerializer, OrderProductSerializerForListOfbuy
from moshfeghi_post_info.models import PostPrice
from .models import Order,OrderDetail
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.authentication import SessionAuthentication

from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView, 
    # RetrieveAPIView, 
    # RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

from django.http.response import HttpResponse, JsonResponse

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
            # print(f"product.priceOff={product.priceOff}")
            if product.priceOff == None:
                order.orderdetail_set.create(product_id=product.id, price=(int(product.price)*int(count)) ,count=count)
            else:
                order.orderdetail_set.create(product_id=product.id, price=(int(product.priceOff)*int(count)) ,count=count)

        # todo: redirect user to user panel
        messages.success(request, "محصول مورد نظر به سبد خرید اضافه شد.")       
        # return redirect('/products')
        return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')

    return redirect('/')



@login_required(login_url='/login')
def List_user_open_order(request):
    # print("kir khar")
    # logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()
    # print("post_price=",post_price.price)
    # print(f"order_partials_buy={order_partials_buy}")
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    username = request.user.username

    contex = {
        'username' : username,
        'order_partials_buy': order_partials_buy,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
    }
    return render(request ,'list_of_buy.html',contex)

class DeleteOrderDetail(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = DeleteOrderDetailSerializer
    permission_classes = [IsAuthenticated]

#! delete product order detail
class Order_product_delete_list_of_buy(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderProductDeleteListOfBuySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, )

    def delete(self, request, *args, **kwargs):

        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        order.orderdetail_set.all().delete()

        # print(f"order_partials_buy={order_partials_buys}")
        return Response({
            "ok":"ok"
        })
    
class product_order_List_buy(UpdateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderProductSerializerForListOfbuy
    permission_classes = [IsAuthenticated]
    # lookup_field = 'id'
    def put(self, request, *args, **kwargs):
        user = request.user
        order = Order.objects.filter(owner=user,is_paid=False).first()
        if order is None:
            order = Order.objects.create( owner=user, is_paid=False)
        orderdetail_product_code = int(request.data.get('id'))
        count = int(request.data.get('count'))

        post_price = PostPrice.objects.filter().first()
        if count < 1:
            count = 1
            
        x = order.orderdetail_set.filter(id=orderdetail_product_code)
        if count > int(x[0].product.number):
            if x:
                if x[0].product.priceOff is None:
                    x.update(price=(x[0].product.number*x[0].product.price))
                else:
                    x.update(price=(count*x[0].product.priceOff))
                x.update(count=x[0].product.number)
            data = {
                'err':'not exist',
                'number': x[0].product.number
            }
            return JsonResponse(data, safe=False, status=201)

        if x:
            #* gheymat ham bayad barrasi shavad
            if x[0].product.priceOff is None:
                x.update(price=(count*x[0].product.price))
            else:
                x.update(price=(count*x[0].product.priceOff))
            x.update(count=count)


        order_partials_buy = order.orderdetail_set.all()

        Total_price_for_all_product_buy =0
        count_of_all_product =0
        count_all=0
        #* barrasi shavad
        # Total_price_for_each_product_buy=0
        for order_partial in order_partials_buy:
            count_of_all_product =count_of_all_product+1
            #* in barrasi shavad
            count_all =count_all +order_partial.count
            
            Total_price_for_each_product_buy = order_partial.price
            Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy

        Total_price_postPrice = Total_price_for_all_product_buy + post_price.price
        # print('count_all=',count_all);
        # print('Total_price_postPrice=',Total_price_postPrice);


        response = {
            "id": x.values()[0]['id'],
            "count": x.values()[0]['count'],
            "price": x.values()[0]['price'],
            "Total_price_for_all_product_buy" : Total_price_for_all_product_buy,
            "count_of_all_product" : count_of_all_product,
            "Total_price_postPrice" : Total_price_postPrice,
            "count_all" : count_all,
        }

        return JsonResponse(response, safe=False)
        return JsonResponse({"response":"ok"}, safe=False)
