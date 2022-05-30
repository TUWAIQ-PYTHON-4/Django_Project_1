from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# Local URL
urlpatterns = [
                  path('home/', views.home, name='home'),
                  path('', views.home, name='home'),
                  path('AddPage/', views.add, name='add'),
                  path('delete/<Tasks_id>', views.delete, name='delete'),
                  path('edit/<Tasks_id>', views.edit, name='edit'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
