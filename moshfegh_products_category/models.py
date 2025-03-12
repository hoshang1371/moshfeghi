from django.db import models

class ProductCategory(models.Model):
    parent = models.ForeignKey(
        'self', 
        default=None, 
        null=True,
         blank=True, 
        on_delete=models.CASCADE,
        related_name='children', 
        verbose_name='زیر دسته')
    title = models.CharField(max_length=150 ,verbose_name='عنوان')
    name = models.CharField(max_length=150 ,verbose_name='عنوان در url')
    # slug = models.SlugField()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title