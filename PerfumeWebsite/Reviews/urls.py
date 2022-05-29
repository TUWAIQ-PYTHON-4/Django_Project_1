from django.urls import path
from . import views

urlpatterns = [
    path('reviews', views.reviews, name='reviews'),
    path('reviews', views.delete, name='reviews'),
    path('reviews', views.fexample, name='reviews'),

]