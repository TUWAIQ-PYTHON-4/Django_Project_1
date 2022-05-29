from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
                  path('', views.home, name='home'),
                  path('add_product', views.add_product, name='add_product'),
                  path('delete_product/<id>/', views.delete_product, name='delete_product'),
                  path('update_product/<id>/', views.update_product, name='update_product'),
                  path('search_product', views.search_product, name='search_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
