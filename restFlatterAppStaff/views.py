from django.shortcuts import render

from rest_framework.authtoken import views as auth_views

from Product.models import Product

from restFlatterAppStaff.permissions import IsStaffOrReadOnly
from restFlatterAppStaff.serializer import MyAuthTokenSerializer, ProductSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import \
    ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # !faal shavad
    # permission_classes = (IsStaffOrReadOnly,)
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (SessionAuthentication, )
    # authentication_classes = (TokenAuthentication, )

# @api_view(['GET'])


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # !faal shavad
    # permission_classes = (IsStaffOrReadOnly,)
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