from django.shortcuts import render
from django.views.generic import ListView

from Product.models import Product
from moshfegh_products_category.models import ProductCategory
from moshfeghi_setting.models import SiteSetting
from django.http import Http404, request

# Create your views here.
def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product_name = kwargs['name']
    print(selected_product_id,product_name)
    context = {

    }   


    return render(request, 'product_detail.html', context)

class ProductList(ListView):
    template_name = 'products_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.get_active_products()

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        #context['cate'] = ProductCategory.objects.filter(title__iexact=Product.title).first()
        #context['cates'] = ProductCategory.objects.order_by('title')
        context['header'] = "محصولات"
        # context['setting'] =SiteSetting.objects.first()
        return context
    
class ProductListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 8

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)

    def get_context_data(self, **kwargs):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        context = super(ProductListByCategory, self).get_context_data(**kwargs)
        context['header'] = category.title
        # context['setting'] =SiteSetting.objects.first()
        return context
    


class SearchProductsView(ListView):
    template_name = 'products_list.html'
    paginate_by = 8
    
    def get_queryset(self):       
        request = self.request
        print("request.GET")
        query = request.GET.get('q')
        if query is not None:
            #print(query)
            #return Product.objects.filter(title__icontains=query)
            return Product.objects.search(query)
        return Product.objects.get_active_products()
    
    def get_context_data(self, **kwargs):
        context = super(SearchProductsView, self).get_context_data(**kwargs)
        #context['cate'] = ProductCategory.objects.filter(title__iexact=Product.title).first()
        #context['cates'] = ProductCategory.objects.order_by('title')
        context['header'] = "جست و جو"
        # context['setting'] =SiteSetting.objects.first()
        return context