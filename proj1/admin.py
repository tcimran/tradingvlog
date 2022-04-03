from django.contrib import admin
from . models import *
# Register your models here.


class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}#to write the slug as per the name given

admin.site.register(Category, catadmin)

class prod(admin.ModelAdmin):
    #this below code displays details of all fields in productadmin panel
    list_display = ['name','slug','price','stock','img']
    list_editable = ['price', 'stock', 'img']
    prepopulated_fields = {'slug': ('name',)}  # to write the slug auto. as per the name given

admin.site.register(product,prod)