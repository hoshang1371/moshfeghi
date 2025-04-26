from Product.serializers import ProductDitailSerializer
from .models import OrderDetail,Order
from rest_framework import serializers



class DeleteOrderDetailSerializer(serializers.ModelSerializer):
    model = OrderDetail
    fields = (
        "id",
        )
    
#! product order detail delete
class OrderProductDeleteListOfBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderProductSerializerForListOfbuy(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        # fields = '__all__'
        fields = ('id','count')

class OrderProductSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.username", read_only=True)
    product = ProductDitailSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = "__all__"
        depth = 1
        # fields = {'product','count'}