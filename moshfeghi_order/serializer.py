from .models import OrderDetail,Order
from rest_framework import serializers



class DeleteOrderDetailSerializer(serializers.ModelSerializer):
    model = OrderDetail
    fields = (
        "id",
        )