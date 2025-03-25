from Product.models import CustomerComment, LikesCustomerComment
from rest_framework import serializers

class CustomerCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        time_calc = serializers.CharField(source='time_calc')
        like_comment_calc = serializers.CharField(source='like_comment_calc')
        # is_liked = serializers.CharField(source='is_liked')
        model = CustomerComment
        fields = (
            "id",
            "user",
            "text",
            "created",
            "updated",
            "time_calc",
            "like_comment_calc",
            # "is_liked",
            "parent",
            "replies",
        )
        depth = 1
        # fields = '__all__'

    def get_fields(self):
        fields = super(CustomerCommentSerializer, self).get_fields()
        fields['replies'] = CustomerCommentSerializer(many=True, read_only=True)
        return fields
    
class DeleteCustomerCommentSerializer(serializers.ModelSerializer):
    model = CustomerComment
    fields = (
        "id",
        )
    
class LikesCustomerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesCustomerComment
        fields = '__all__'