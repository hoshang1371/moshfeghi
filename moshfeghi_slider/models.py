from django.db import models

import os
from django.conf import settings

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sliders/{final_name}"

class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان', null=True, blank=True)
    #titleOnSlider = models.CharField(max_length=120, verbose_name=' عنوان روی اسلایدر')
    link = models.URLField(max_length=100,verbose_name='ادرس', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    price = models.IntegerField(verbose_name='قیمت')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
    


class SliderDown(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان', null=True, blank=True)
    link = models.URLField(max_length=100,verbose_name='ادرس', null=True, blank=True)
    description1 = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    imageSlider = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر پایین'
        verbose_name_plural = 'اسلایدرها پایین'

    def __str__(self):
        return self.title
    
    def get_image_SliderDown(self):
        if self.imageSlider:
            #! in url bayad avaz shavad
            return settings.ALLOWED_HOSTS[0] + self.imageSlider.url
            # return 'http://127.0.0.1:8000' + self.imageSlider.url
        return ''