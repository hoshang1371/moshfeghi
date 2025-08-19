from django.shortcuts import render

from rest_framework.authtoken import views as auth_views

from Product.models import Product

from moshfeghi_order.models import Order, OrderDetail
from restFlatterAppStaff.permissions import IsStaffOrReadOnly
from restFlatterAppStaff.serializer import MyAuthTokenSerializer, OrderDeleteSerializer, OrderProductDeleteSerializer, OrderProductSerializer, OrderProductUpdateSerializer, ProductSerializer, SearchProductSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import \
    ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView,\
    UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from rest_framework.decorators import permission_classes

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # !faal shavad
    permission_classes = (IsStaffOrReadOnly,)
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (SessionAuthentication, )
    # authentication_classes = (TokenAuthentication, )

# @api_view(['GET'])


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # !faal shavad
    permission_classes = (IsStaffOrReadOnly,)
    # permission_classes = [IsAuthenticated]



class EmailToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)

class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = MyAuthToken.as_view()


#!check Token
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def CheckToken(request):
    if request.method == 'POST':
        # print(type(request.data))
        # print(request.data["token"])
        if Token.objects.filter(pk=request.data["token"]).exists():
            user = Token.objects.get(pk=request.data["token"]).user
            print(user.id)
            # return Response(request.data)
            return Response(
                {
                    'token': request.data["token"],
                    # 'token': token.key,
                    'username': user.username,
                    'userid': user.id
                })
        else:
            return Response({"token": "token is distroy"})
    return Response({"message": "Hello, world!"})


#! product order staff
# Sample.objects.filter(date__range=[startdate, enddate]) payment_date


class product_order_staff(ListCreateAPIView):
    serializer_class = OrderProductSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        startdate = datetime.today()
        enddate = startdate - timedelta(days=6)
        # print(startdate)
        # print(enddate)
        # order = Order.objects.filter(owner_id=self.request.user.id)
        # order1 = Order.objects.filter(payment_date__range=["2022-10-23", "2022-10-29"])
        # print(order1)
        order = Order.objects.filter(Q(owner_id=self.request.user.id) & Q(
            payment_date__range=[enddate, startdate])).all()
        #! ehtemalan inja irad dare va bayad do khat zir az halat kament kharej shavad
        # if order is None:
        #     order = Order.objects.create(owner_id=request.user.id, is_paid=False)        
        response = []
        for val in order.values():
            v = {
                "id": val['id'],
                "owner": val['owner_id'],
                "is_paid": val['is_paid'],
                "payment_date": str(val['payment_date']),
                "j_payment_date": str(val['j_payment_date'])
            }
            response.append(v)
        return JsonResponse(response, safe=False)
        # return JsonResponse(json.dumps(response), safe=False)

        # return JsonResponse(response)
        # return Response(response)
        # return Response({"message": "Hello, world!"})

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(
            owner_id=self.request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=self.request.user.id, is_paid=False)
        product_id = int(request.data.get('product'))
        count = int(request.data.get('count'))
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        # print(type(count))
        # print(type(int(product.number)))
        if count > int(product.number):
            # print("in tedad dar anbar mojod nist")
            return JsonResponse({
                    "massege": "no this count exist",
                    })
        else:
            print("mojod dar anbar ast")
        print("tedad",product.number)
        #TODO : chek kardadn tedad
        x = order.orderdetail_set.filter(product_id=product.id)
        if x:
            print("exist")
            print(x.values()[0]['count'])
            # x.update(count=count+x.values()[0]['count'])
            x.update(count=count)
        else:
            print("NO exist")
            order.orderdetail_set.create(
                product_id=product.id, price=product.price, count=count)
           # TODO
        return Response(request.data)
 
#! product list order staff


class product_order_ditails_staff(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        orderDetails = OrderDetail.objects.filter(order=order_id)
        response = []
        total_price = 0
        for orderDetail in orderDetails:
            product = Product.objects.filter(title=orderDetail.product)
            print(orderDetail.price * orderDetail.count)
            total_price = total_price + (orderDetail.price * orderDetail.count)
            v = {
                "id_order": orderDetail.id,
                "orderDetail_count_price": orderDetail.price * orderDetail.count,
                "id": product[0].id,
                "code": product[0].code,
                "title": product[0].title,
                "place": product[0].place,
                "count": orderDetail.count,
                "brand": product[0].brand,
                "description": product[0].description,
                "smallDescription": product[0].smallDescription,
                "price": product[0].price,
                "priceOff": product[0].priceOff,
                "image": product[0].image.url,
                "image_tumpnail": product[0].image_tumpnail.url,
                "active": str(product[0].active).lower(),
                "visit_count": product[0].visit_count,
                "vige": str(product[0].vige).lower(),

            }
            response.append(v)
        print("total_price", total_price)
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})   
    
#! search
# http://192.168.1.51:8000/api/questions/?search=
# @api_view(['GET'])


class SearchProductAPIView(generics.ListCreateAPIView):
    #search_fields = ['title','description','smallDescription']
    search_fields = ['title', 'code', 'place']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer


class SearchProductWithOnlyPlaceAPIView(generics.ListCreateAPIView):
    #search_fields = ['title','description','smallDescription']
    search_fields = ['place']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer

#! delete product order detail
class product_order_delete_staff(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderProductDeleteSerializer
    permission_classes = (IsAdminUser,)

#! delete product order detail
class order_delete_staff(DestroyAPIView):
    queryset = Order.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderDeleteSerializer
    permission_classes = (IsAdminUser,)

    
class isPaid_order_update_staff(UpdateAPIView):
    queryset = Order.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    serializer_class = OrderProductUpdateSerializer
    lookup_field = 'id'
    permission_classes = (IsAdminUser,)


    def put(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        order = Order.objects.filter(
            owner_id=self.request.user.id, is_paid=False).first()
        
        orderDetails = order.orderdetail_set.filter(order=order)
        for orderDetail in orderDetails:
            # print(orderDetail.count)
            # print(orderDetail.product.number)
            # print(orderDetail.product)
            # ToDo: شاید باید بررسی بشه که تعداد داخل انبار از تعداد سفارش ها کمتر نباشد
            orderDetail.product.number = int(orderDetail.product.number)-orderDetail.count
            # print(orderDetail.product.number)
            orderDetail.product.save()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

