from django.urls import path
from . import views

app_name= "view"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('show-reviews/', views.show_review, name='show_review'),
    path('add-review/', views.add_review, name='add_review')
]
