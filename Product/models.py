from django.db import models

from extentions.images import make_thumbnail

import os

from moshfegh_products_category.models import ProductCategory
from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()
from django_jalali.db import models as jmodels
import jdatetime
import convert_numbers

import pytz
# from django.http import request
from extentions.time import getDuration

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_image_tumpnail_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products\\tumpnail\\{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self ,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name ,active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self,query):
        lookup = (
                    Q(title__icontains=query) | 
                    Q(description__icontains=query)
                    #! baadan faal shavad
                    #|Q(tag__title__icontains=query)
                    )
        return self.get_queryset().filter(lookup, active=True).distinct()

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    code = models.CharField(max_length=150, verbose_name='کد')
    place = models.CharField(max_length=150, verbose_name='مکان کالا', null=True, blank=True)
    number = models.CharField(max_length=150, verbose_name='تعداد', null=True, blank=True)
    brand = models.CharField(max_length=150, verbose_name='برند', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    smallDescription = models.TextField(max_length=150,verbose_name='کوتاه توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    priceOff = models.IntegerField(verbose_name='قیمت تخفیف', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    image_tumpnail = models.ImageField(upload_to= upload_image_tumpnail_path, null=True, blank=True, verbose_name='تصویر_بند_انگشتی')
    #image_tumpnail = ResizedImageField(upload_to= upload_image_tumpnail_path, size=[150, 100], null=True, blank=True, verbose_name='تصویر_بند_انگشتی')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank =True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید ها')
    vige = models.BooleanField(default=False, verbose_name='ویژه / غیرویژه')
#"image": "G:'\kartmelli.jpg"
    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        # print(f"image : {self.image}")
        make_thumbnail(self.image_tumpnail, self.image, (50, 50), 'thumb')
        super(Product, self).save(*args, **kwargs)

    



class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title
    

class CustomerComment(models.Model):

    CommentProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول پیام')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر پیام')

    parent = models.ForeignKey(
        'self', 
        default=None, 
        null=True, 
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies', 
        verbose_name='زیر دسته')
    text = models.TextField(verbose_name='متن پیام',
                            null=True, blank=True)
    

    created = jmodels.jDateTimeField(auto_now_add=True,blank = True, null = True, verbose_name='تاریخ ایجاد پیام شمسی')
    updated = jmodels.jDateTimeField(auto_now=True,blank = True, null = True, verbose_name='تاریخ تغییر پیام شمسی')

    is_ok = models.BooleanField(verbose_name='تایید شده / نشده' ,default=False)


    def time_calc(self):
        now = jdatetime.datetime.utcnow().replace(tzinfo=pytz.timezone('Asia/Tehran')) 
        return getDuration(self.updated, now)

    def like_comment_calc(self):
        numberLikeC =LikesCustomerComment.objects.filter(CustomerComment_id=self.id,CustomerComment__CommentProduct_id=self.CommentProduct.id,likes=True).count()
        return(convert_numbers.english_to_persian(str(int(numberLikeC))))
    
    def is_liked(self):
        a = False
        # request = args[0] if args else kwargs.get('request') or self.request
        # isLiked =LikesCustomerComment.objects.filter(user=1,CustomerComment_id=self.id,CustomerComment__CommentProduct_id=self.CommentProduct.id,likes=True).first()
        # print(request.user)
        return(a)
    

    
    class Meta:
        verbose_name = ' نظرات کاربران '
        verbose_name_plural='نظرات در مورد کالا کاربران'

    def __str__(self):
        return self.text
    

class LikesCustomerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CustomerComment = models.ForeignKey(CustomerComment, on_delete=models.CASCADE,related_name='isLiked', )
    likes = models.BooleanField(default=False)


    
    class Meta:
        unique_together = ('user', 'CustomerComment',)
        verbose_name = 'پسندیدن نظرات'
        verbose_name_plural = 'پسندیدن نظرات'