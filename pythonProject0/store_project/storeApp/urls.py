from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.home,name='home'),
     path('feedback', views.form_feedback,name='feedback'),
     path("add/", views.add_products, name="add_products"),
     path('delete/<Products_id>', views.delete, name='delete'),
     path('edit/<Products_id>', views.edit, name='edit'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)