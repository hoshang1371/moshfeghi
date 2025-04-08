import datetime

from moshfegh_products_category.models import ProductCategory
from moshfeghi_setting.models import SiteSetting
from moshfeghi_order.models import Order,OrderDetail


def custom_context_processor(request):
    # Define your context variables here
    # categorys = ProductCategory.objects.all() 
    categorys = ProductCategory.objects.filter(parent__isnull=True)
    site_setting = SiteSetting.objects.first()
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    orderDetails = OrderDetail.objects.filter(order=order)
    # print(f"order={order}")
    # print(f"orderDetails={orderDetails}")
    totalCount = 0
    for orderDetail in orderDetails:
        totalCount += orderDetail.count 
    # print(totalCount)
    # print(f"categorys ={categorys}")
    return {
        'categorys': categorys,
        'site_setting':site_setting,
        'orderDetails': orderDetails,
        'totalCount': totalCount,
        # 'user_agent': request.META.get('HTTP_USER_AGENT', ''),
    }