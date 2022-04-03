from django.urls import path
from . import views

urlpatterns=[
    path('cartdet',views.cart_det,name='cartdet'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('min/<int:product_id>/',views.min_cart,name='min_cart'),
    path('del/<int:product_id>/',views.del_cartitems,name='del_cart'),
]