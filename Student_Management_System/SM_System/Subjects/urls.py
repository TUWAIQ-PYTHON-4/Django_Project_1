from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.subjects_base, name='subjects'),
    path('delete_subject/<list_id>', views.delete_subject, name='delete_subject'),
    path('edit_subject/<list_id>', views.edit_subject, name='edit_subject')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)