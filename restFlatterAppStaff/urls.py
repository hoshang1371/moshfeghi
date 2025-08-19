from django.urls import path, include


from .views import CheckToken, ProductDetail, ProductList, SearchProductAPIView,\
SearchProductWithOnlyPlaceAPIView, isPaid_order_update_staff, obtain_auth_token, order_delete_staff, product_order_delete_staff, product_order_ditails_staff, product_order_staff

app_name = "api"


urlpatterns = [

    # path('core', apage),
    path("",ProductList.as_view(), name="list"),
    path("<int:pk>",ProductDetail.as_view(), name="detail"),
    #!product order staff url
    path('product_order_staff/', product_order_staff.as_view()),
    # path("user/",UsertList.as_view(), name="user-list"),
    # path("user/<int:pk>",UserDetail.as_view(), name="user-detail"),

    # #! Revoke Token
    # path('revoke',RevokeToken.as_view()),
    #!login with email
    path('api_token_auth/', obtain_auth_token),
    #!search url
    path('questions/', SearchProductAPIView.as_view()),
    #! check Token
    path('Check_token/', CheckToken),
    #!search url
    path('questions/', SearchProductAPIView.as_view()),
    #!search with only place url
    path('questionsForPlace/', SearchProductWithOnlyPlaceAPIView.as_view()),
    #!product order staff url
    path('product_order_staff/', product_order_staff.as_view()),
    #!product order ditails staff url
    path('product_order_ditails_staff/<order_id>/', product_order_ditails_staff.as_view()),
        #!product order delete staff url
    path('product_order_delete_staff/<int:pk>/delete', product_order_delete_staff.as_view()),
    #!product order delete staff url
    path('order_delete_staff/<int:pk>/delete', order_delete_staff.as_view()),
    path('isPaid_order_update_staff/update/<int:id>/', isPaid_order_update_staff.as_view()),
    #!dj_rest_auth
]