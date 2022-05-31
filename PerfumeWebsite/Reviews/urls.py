from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.index, name='index'),
    path('add/', views.add_rev, name='add_rev'),
    path('delete/<reviews_id>', views.delete, name='delete'),
    path('edit/<reviews_id>', views.edit, name='edit'),

]