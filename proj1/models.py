from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse #to create urls slugfields in urls
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True,null=False)
    slug=models.SlugField(max_length=250)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    dsc=models.TextField()
    stock=models.IntegerField(null=False)
    avail=models.BooleanField()
    price=models.IntegerField(null=False)
    catname=models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('itemsdet',args=[self.catname.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)

