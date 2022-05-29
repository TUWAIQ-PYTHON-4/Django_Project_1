from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'brands'
urlpatterns = [
                  path('add_brand', views.add_brand, name='add_brand'),
                  path('brand_list', views.brand_list, name='brand_list'),
                  path('show_brand/<brand_id>', views.show_brand, name='show_brand'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
