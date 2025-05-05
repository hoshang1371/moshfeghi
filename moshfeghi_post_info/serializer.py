from rest_framework import serializers

from moshfeghi_post_info.models import PostAddress



#! product order delete
class PostAddressDeleteListOfBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAddress
        fields = '__all__'