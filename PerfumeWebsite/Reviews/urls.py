from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_f, name='reviews_f'),
    path('reviews_list/<id>/', views.reviews_list, name='reviews_list'),
    path('delete/<id>/', views.delete, name='delete'),

]