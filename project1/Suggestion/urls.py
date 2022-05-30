from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('form',views.home, name='form'),
    path('form/add',views.add, name='form/add'),
    path('delete/<name_id>', views.delete, name='delete'),
    path('edit/<name_id>', views.edit, name='edit')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)