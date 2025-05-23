from django.urls import path

from moshfeghi_post_info.views import PostAddress_delete_list_of_buy, post_add_address, post_order,add_userPostAddressDetail, send_code_for_varify_mobile_address



urlpatterns = [
    path('سفارش', post_order ,name="post_order"),
    path('add_userPostAddressDetail', add_userPostAddressDetail ,name="add_userPostAddressDetail"),
    path('PostAddress_delete_list_of_buy/<int:pk>', PostAddress_delete_list_of_buy.as_view()),
    path('post_add_address', post_add_address ,name="post_add_address"),
    path('send_code_for_varify_mobile_address', send_code_for_varify_mobile_address.as_view() ,name="sendCodeForVarifyMobileAddress"),

]