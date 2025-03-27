from django.shortcuts import render
from django.views.generic import ListView

from Product.models import CustomerComment, LikesCustomerComment, Product, ProductGallery
from Product.serializers import CustomerCommentSerializer, DeleteCustomerCommentSerializer, LikesCustomerCommentSerializer
from moshfegh_products_category.models import ProductCategory
from moshfeghi_setting.models import SiteSetting
from django.http import Http404, request

import itertools
from rest_framework.response import Response

from rest_framework.generics import DestroyAPIView,ListAPIView,CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import convert_numbers
from random import randint

# from django import template
# from django.template.defaultfilters import stringfilter

# register = template.Library()



# from django.db.models import F

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

# @register.filter
# def comment_isliked(comment,request):
#     return comment.isLiked.filter(user=request.user).first()

# Create your views here.
def product_detail(request, *args, **kwargs):

    selected_product_id = kwargs['productId']
    product_name = kwargs['name']

    # TODO

    product = Product.objects.get_by_id(selected_product_id)
    comments = CustomerComment.objects.filter(CommentProduct=product,parent__isnull=True)
# childe
    test_cats = ProductCategory.objects.all()
    #! این فیلتر اشتباه است از سر فرصت درست شود
    best_sellers = Product.objects.all().filter(active=True).order_by('-visit_count')[0:10]
    random_products = Product.objects.order_by('?')[:5]
    # print(random_producr)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    
    product.visit_count += 1
    product.save()
    # print(test_cat)
    # print(product.categories.all()[0].children.all())

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)

    # print(galleries)
    galleries_idx = list(zip(galleries, range(0, len(galleries)+1)))
    # for idx, x in enumerate(galleries):
    #     print(idx, x)

    # print(galleries_idx)
    # for g in galleries:
    #     print(g.id)
    # grouped_galleries = list(my_grouper(1, galleries))

    context = {
        'product': product,
        'galleries' : galleries_idx,
        'comments' : comments,
        'best_sellers' : best_sellers,
        # 'related_products' : related_products,
        'random_products' : random_products,


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
        # #! in dorost shavad
        # print("category.children")
        # print(category)
        # print(category.children.all().first())
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
    



class DeleteCustomerComment(DestroyAPIView):
    queryset = CustomerComment.objects.all()
    serializer_class = DeleteCustomerCommentSerializer
    permission_classes = [IsAuthenticated]

class CustomerCommentClass(ListAPIView):
    queryset = CustomerComment.objects.all()
    serializer_class = CustomerCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostCustomerComment(CreateAPIView):   
    # serializer_class = PostCustomerCommentSerializer
    serializer_class = CustomerCommentSerializer
    queryset = CustomerComment.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user.id
        comments = CustomerComment.objects.create(
            user_id= user,
            CommentProduct_id=request.data["product"],
            text=request.data["text"],
            is_ok=False,
            parent_id=request.data["parent"],
        )
        
        return Response({
            "ok":"ok"
        })
    
#TODO: change ListCreateAPIView
class LikesCustomerCommentClass(ListCreateAPIView):
    queryset = LikesCustomerComment.objects.all()
    serializer_class = LikesCustomerCommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request,CustomerComment_id, *args, **kwargs):
        user = request.user
        if LikesCustomerComment.objects.filter(user=user,CustomerComment_id=CustomerComment_id).exists():
            likC = LikesCustomerComment.objects.filter(user=user,CustomerComment_id=CustomerComment_id).first()

        else:
            likC = LikesCustomerComment.objects.create(user=user,CustomerComment_id=CustomerComment_id)

        likC.likes = not likC.likes
        likC.save()
        numberLikeC = LikesCustomerComment.objects.filter(CustomerComment_id=CustomerComment_id,likes=True)
        return Response({
            "like" : likC.likes,
            "numberLike": convert_numbers.english_to_persian(str(numberLikeC.count()))
        })