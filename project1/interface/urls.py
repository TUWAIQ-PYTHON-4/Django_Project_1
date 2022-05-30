from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.base, name='base'),
    path('',views.home, name='home'),
    path('products',views.Product,name='products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)