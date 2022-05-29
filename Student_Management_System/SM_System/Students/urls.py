from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.students_base, name='students'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('show_student_subjects/<list_id>', views.show_student_subjects, name='show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)