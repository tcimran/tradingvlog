
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecom/home/',include('accounts.urls')),
    path('ecom/home/',include('cart.urls')),
    path('ecom/',include('proj1.urls')),


]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)