from django.urls import path

from moshfeghi_post_info.views import PostAddress_delete_list_of_buy, RegisterPaymentInformation, cartToCartPeyment, edit_post_add_address, paymentMethod, pdf_factor, post_add_address, post_order,add_userPostAddressDetail, send_code_for_varify_mobile_address



urlpatterns = [
    path('سفارش', post_order ,name="post_order"),
    path('add_userPostAddressDetail', add_userPostAddressDetail ,name="add_userPostAddressDetail"),
    path('PostAddress_delete_list_of_buy/<int:pk>', PostAddress_delete_list_of_buy.as_view()),
    path('post_add_address', post_add_address ,name="post_add_address"),
    path('paymentMethod', paymentMethod ,name="paymentMethod"),
    path('cartToCartPeyment', cartToCartPeyment ,name="cartToCartPeyment"),

    path('send_code_for_varify_mobile_address', send_code_for_varify_mobile_address.as_view() ,name="sendCodeForVarifyMobileAddress"),
    path('edit_post_add_address/<int:pk>', edit_post_add_address ,name="edit_post_add_address"),

    path('pdf_factor/<int:pk>', pdf_factor ,name="pdf_factor"),
    path('RegisterPaymentInformation/<int:pk>', RegisterPaymentInformation ,name="RegisterPaymentInformation"),

]