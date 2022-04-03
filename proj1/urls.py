from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('<slug:c_slug>/<slug:product_slug>',views.prod_det,name='itemsdet'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('search',views.searching,name='search'),




]