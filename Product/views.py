from django.shortcuts import render
from django.views.generic import ListView

from Product.models import Product, ProductGallery
from moshfegh_products_category.models import ProductCategory
from moshfeghi_setting.models import SiteSetting
from django.http import Http404, request

import itertools

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))
# Create your views here.
def product_detail(request, *args, **kwargs):

    selected_product_id = kwargs['productId']
    product_name = kwargs['name']

    # TODO
    # new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    # contact_form_comment = CustomersCommentsForm(request.POST or None)

    # print(selected_product_id,product_name)
    product = Product.objects.get_by_id(selected_product_id)

    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    
    product.visit_count += 1
    product.save()


    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    # grouped_related_products = list(my_grouper(3, related_products))

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)

    print(galleries)
    galleries_idx = list(zip(galleries, range(0, len(galleries)+1)))
    # for idx, x in enumerate(galleries):
    #     print(idx, x)

    print(galleries_idx)
    # for g in galleries:
    #     print(g.id)
    # grouped_galleries = list(my_grouper(1, galleries))

    context = {
        'product': product,
        'galleries' : galleries_idx,
        # 'galleries_2' : galleries_idx,
        'related_products' : related_products,
        # 'customercomments' : customercomments,


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