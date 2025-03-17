from django.urls import path

from .views import ProductList, ProductListByCategory, SearchProductsView, product_detail

urlpatterns = [
    path('<productId>/<name>', product_detail),
    path('list', ProductList.as_view(), name="product_list"),
    path('search', SearchProductsView.as_view()),
    path('<category_name>', ProductListByCategory.as_view()),
]