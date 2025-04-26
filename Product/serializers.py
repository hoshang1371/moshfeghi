from Product.models import CustomerComment, LikesCustomerComment, Product
from moshfegh_products_category.models import ProductCategory
from rest_framework import serializers
import convert_numbers

    
class ProductDitailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "number",
            # "get_absolute_url",
            "description",
            "smallDescription",
            "price",
            "priceOff",
            "categories",
            "visit_count",
            # "get_image",
            # "int_average_rating",
            # "float_average_rating",
            # "get_thumbnail",
            "get_absolute_url",
            )


    def get_parnt_category(self,serial,categ=[]):

        category = ProductCategory.objects.filter(pk=serial).first()

        if category.parent != None:
            cat = category.parent.id
            a ={
                "title":category.title,
                "link":category.name
            }
            categ.append(a)

            self.get_parnt_category(serial=cat,categ=categ)
        else:
            a ={
                "title":category.title,
                "link":category.name
            }
            categ.append(a)
        # finalCat = categ
        # categ =[]
        return(categ)

  
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = convert_numbers.english_to_persian(str(representation['price']))
        if representation['priceOff'] != None:
            representation['priceOff'] = convert_numbers.english_to_persian(str(representation['priceOff']))

        if representation['categories'] != []:
            cat = representation['categories'][0]
            categories= self.get_parnt_category(cat,categ=[])
            # print(f"categories={representation['categories']}")
            representation['categories'] = categories
        # # print(f'categories={categories}')
        return representation
  


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