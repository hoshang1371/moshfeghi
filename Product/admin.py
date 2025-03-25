from django.contrib import admin

# Register your models here.
from .models import CustomerComment, LikesCustomerComment, Product ,ProductGallery

@admin.register(CustomerComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'CommentProduct', 'created', 'is_ok')
    list_filter = ('is_ok', 'created', 'updated')
    search_fields = ('user', 'text')


@admin.register(LikesCustomerComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'CustomerComment', 'likes')
    list_filter = ('user', 'CustomerComment', 'likes')
    search_fields = ('user', 'CustomerComment','likes')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    # def delete_link(self, obj):
    #     info = obj._meta.app_label, obj._meta.module_name
    #     url = reverse('admin:%s_%s_delete' % info, args=(obj.id,))
    #     return '<a href="%s">Delete</a>' % url
        
    # delete_link.allow_tags = True
    # delete_link.short_description = 'Delete'

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)