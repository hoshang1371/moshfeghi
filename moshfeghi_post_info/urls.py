from django.urls import path

from moshfeghi_post_info.views import post_order,add_userPostAddressDetail



urlpatterns = [
    path('سفارش', post_order ,name="post_order"),
    path('add_userPostAddressDetail', add_userPostAddressDetail ,name="add_userPostAddressDetail"),

]