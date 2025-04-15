from django.urls import path
from moshfeghi_order.views import DeleteOrderDetail, add_user_order, \
    List_user_open_order #, user_open_order, remove_order_detail

urlpatterns = [
    path('add-user-order', add_user_order),
    path('Delete_product_orderDetail/<int:pk>/',DeleteOrderDetail.as_view()),
    path('list_for_buy', List_user_open_order ,name="buyList"),

    # path('open-order', user_open_order),
    # path('remove-order-detail/<detail_id>', remove_order_detail)
]