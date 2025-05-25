import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from moshfeghi_order.models import Order
from moshfeghi_post_info.forms import AddAddress, CarrierChoices, Country, UserPostAddressDetailForm
from moshfeghi_post_info.models import PostAddress, PostAddressDetail, PostPrice
from moshfeghi_post_info.serializer import PostAddressDeleteListOfBuySerializer
from new_account.models import UserCode
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from django.http import JsonResponse
from extentions.sendSmsRandom import random_with_N_digits,sendSmsForVarifyAddress,sendSms

User = get_user_model()

from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
def post_order(request):
    postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    #! forms of postaddress
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    # if request.method == 'POST':
    if user_post_address_detail.is_valid():
        product_id = user_post_address_detail.cleaned_data.get('PostAddress_id')
        print('product_id=',product_id)
    #!
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    # print('user_post_address_detail=',user_post_address_detail['PostAddress_id'])
    # username = request.user.username
    # print(f"postAddressUser={(postAddressesUser[0].get_country_display())}")
    contex = {
        # 'order_partials_buy': order_partials_buy,
        # 'username' : username,
        'postAddressesUser' : postAddressesUser,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
        'user_post_address_detail':user_post_address_detail['PostAddress_id'],
        'zipee' : zip(user_post_address_detail['PostAddress_id'],postAddressesUser),
    }
    return render(request ,'post_order.html',contex)



@login_required(login_url='/login')
def add_userPostAddressDetail(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    # postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    carriersChoices = CarrierChoices(request.POST or None,request.user)
    print('user_post_address_detail.choices[0][0]=',user_post_address_detail.choices[0][0])
    if request.method == 'POST':        
        if user_post_address_detail.is_valid():
            PostAddress_id = user_post_address_detail.cleaned_data.get('PostAddress_id')
            print("PostAddress_id=",PostAddress_id)
            # Todo:save to database
            post_address =PostAddress.objects.filter(owner_id=request.user.id,id=PostAddress_id)
            # print("postAddressesUser=",postAddressesUser)
            # print("post_address=",post_address)
            # print("post_address=",post_address[0].address)
            # print("post_address.id=",post_address[0].id)
            # print("order.id=",order.id)

            # post_address_detail = PostAddressDetail.objects.filter(
            #     # addressSelected = 1,
            #     # isResive =False,
            #     # OrderDetailSelected =64,
            # )


            # post_address_detail = post_address.postaddressdetail_set.create(

            post_address_detail = PostAddressDetail.objects.filter(
                                OrderDetailSelected =order,
                                ).first()
            print('post_address_detail=', post_address_detail)

            if post_address_detail is None:
                post_address_detail = PostAddressDetail.objects.create(
                    addressSelected = post_address[0],
                    OrderDetailSelected =order,
                    isResive =False,
                    ) 
            else:
                post_address_detail.addressSelected = post_address[0]
                post_address_detail.save()
                print('post_address_detail.addressSelected=', post_address_detail.addressSelected.id)




    # order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    # print('user_post_address_detail=',user_post_address_detail['PostAddress_id'])
    # username = request.user.username

    contex ={
        # 'username' : username,
        # 'user_post_address_detail': user_post_address_detail,
        # 'postAddressesUser' : postAddressesUser,
        'carriersChoices' : carriersChoices['Carrier_field'],

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,

        # 'zipee' : zip(user_post_address_detail.choices,postAddressesUser),
        
    }
    return render(request ,'add_userAdressDetail.html',contex)


#! delete PostAddress detail
class PostAddress_delete_list_of_buy(DestroyAPIView):
    queryset = PostAddress.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = PostAddressDeleteListOfBuySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, )

@login_required(login_url='/login')
def post_add_address(request):

    # user = User.objects.get(id=request.user.id)
    user = User.objects.get(id=request.user.id)
    add_address = AddAddress(request.POST or None)
    # global stop_threads_sendSmsVarify
    # stop_threads_sendSmsVarify = True
    user_code = UserCode.objects.filter(user=user).first()
    print("kirkhar")

    if request.method == 'POST':
        if add_address.is_valid():
            first_name_for_post = add_address.cleaned_data.get('first_name_for_post')
            last_name_for_post = add_address.cleaned_data.get('last_name_for_post')
            Country_for_post = add_address.cleaned_data.get('Country_for_post')
            City_for_post = add_address.cleaned_data.get('City_for_post')
            Address_for_post = add_address.cleaned_data.get('Address_for_post')
            phone_number_for_post = add_address.cleaned_data.get('phone_number_for_post')
            global mobile_phone_number_for_post
            mobile_phone_number_for_post = add_address.cleaned_data.get('mobile_phone_number_for_post')
            check_mobile_phone_number_for_post = add_address.cleaned_data.get('check_mobile_phone_number_for_post')
            post_code_for_post = add_address.cleaned_data.get('post_code_for_post')

            deffTime =int(datetime.datetime.now(datetime.timezone.utc).timestamp()-user_code.codeVarifySmsDate.timestamp())

            if(deffTime < 120):
            #! check mobile number
                if user_code.codeVarifySms == check_mobile_phone_number_for_post:
                    PostAddress.objects.create(
                            owner_id= request.user.id,
                            firstName = first_name_for_post,
                            lastName = last_name_for_post,
                            country = Country[0][1],
                            city = City_for_post,
                            address = Address_for_post,
                            phone_number = phone_number_for_post,
                            mobile_phone_number = mobile_phone_number_for_post,
                            post_code = post_code_for_post,
                            isCorrect_mobile_phone_number = True
                            )
                    # print("redirect")
                    return redirect('/post_info/سفارش')
            
            messages.success(request, 'کد ارسالی صحیح نمیباشد')
            return redirect('/post_info/post_add_address')      


        

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0
    post_price = PostPrice.objects.filter().first()



    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy

    contex ={

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'count_off_all_product': count_off_all_product,
        'post_price': post_price.price,

        'add_address' : add_address,

    }
    return render(request ,'add_post_address.html',contex)


#!send code for varify mobile address
class send_code_for_varify_mobile_address(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, )

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        mobNumber =request.data.get('mobNum')
        # print(request.data.get('mobNum'))
        if mobNumber=='':
            # TODO : ارور برای وارد کردن شماره موبایل
            # messages.success(request, 'لطفاً شماره موبایل را وارد کنید.')
            # print("not ok")
            return JsonResponse({"mobNum": "not ok"},status=201)
        #globalValue.code = ''

        #globalValue.code = random_with_N_digits(5)

        user_code = UserCode.objects.filter(user=user).first()
        print(f"user_code={user_code}")
        if user_code is None:
            user_code = UserCode.objects.create(
                user = user,
                codeVarifySms = random_with_N_digits(5),
                codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
            )
        else:
            user_code.codeVarifySms = random_with_N_digits(5)   
            user_code.codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
            user_code.save() 
        # print(user_code.codeVarifySms)
        # print(user_code.codeVarifySmsDate)
        
        # user.UserCode.codeVarifySms = random_with_N_digits(5)
        # user.UserCode.codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
        # user.UserCode.save()

        sendSms(user_code.codeVarifySms,mobNumber)
        
        #print('send_code_for_varify_mobile_addressCode=',globalValue.code)
        #global stop_threads_sendSmsVarify
        #stop_threads_sendSmsVarify = False
        #sendSmsVarify = threading.Thread(
         #       target=sendSmsForVarifyAddress, 
          #      args=(
           #         self.request.user,
            #        lambda : stop_threads_sendSmsVarify,
             #       )
              #  )
        #sendSmsVarify.start()

        return JsonResponse({'mobNum':'ok'})

    def get(self, request, *args, **kwargs):
        # print('nanat o sag gaiid')
        #print(self.request.user)
        #print(request.body)
        # global code
        # code = random_with_N_digits(5)
        # print('send_code_for_varify_mobile_addressCode=',code)
        #globalValue.code = ''
        #globalValue.code = random_with_N_digits(5)
        #print('send_code_for_varify_mobile_addressCode=',globalValue.code)

        #global stop_threads_sendSmsVarify
        # stop_threads_sendSmsVarify = True
        #stop_threads_sendSmsVarify = False
        # print(stop_threads_sendSmsVarify)
        #sendSmsVarify = threading.Thread(
         #       target=sendSmsForVarifyAddress, 
          #      args=(
           #         self.request.user,
            #        lambda : stop_threads_sendSmsVarify,
             #       )
              #  )
        #sendSmsVarify.start()
        # stop_threads_sendSmsVarify = True

        return JsonResponse({'foo':'bar'})
