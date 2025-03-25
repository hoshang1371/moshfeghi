from django.urls import path

from .views import DeleteCustomerComment, LikesCustomerCommentClass, ProductList, ProductListByCategory, \
                    SearchProductsView, product_detail, CustomerCommentClass \
                    , PostCustomerComment

urlpatterns = [
    path('<productId>/<name>', product_detail),
    path('list', ProductList.as_view(), name="product_list"),
    path('search', SearchProductsView.as_view()),
    path('<category_name>', ProductListByCategory.as_view()),
    path('api/DeleteCustomerComment/<int:pk>/',DeleteCustomerComment.as_view()),
    path('GetCustomerComment/',CustomerCommentClass.as_view()),
    path('api/PostCustomerComment/',PostCustomerComment.as_view()),
    path('api/GetLikesCustomerComment/<slug:CustomerComment_id>',LikesCustomerCommentClass.as_view()),

]