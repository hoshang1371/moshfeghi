from django.contrib import admin

from moshfeghi_post_info.models import PostAddressDetail, PostPrice,PostAddress,PaymentMethodeDetail

class PostPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','title', 'price']

admin.site.register(PostPrice,PostPriceAdmin)
admin.site.register(PostAddress)
admin.site.register(PostAddressDetail)
admin.site.register(PaymentMethodeDetail)