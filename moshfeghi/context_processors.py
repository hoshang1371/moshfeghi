import datetime

from moshfegh_products_category.models import ProductCategory
from moshfeghi_setting.models import SiteSetting


def custom_context_processor(request):
    # Define your context variables here
    categorys = ProductCategory.objects.all()
    site_setting = SiteSetting.objects.first()
    # print(f"categorys ={categorys}")
    return {
        'categorys': categorys,
        'site_setting':site_setting,
        # 'current_year': datetime.now().year,
        # 'user_agent': request.META.get('HTTP_USER_AGENT', ''),
    }