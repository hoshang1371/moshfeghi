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