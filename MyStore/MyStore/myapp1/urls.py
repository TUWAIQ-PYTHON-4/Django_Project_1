from . import views
from django.urls import path

urlpatterns = [
    path('user-list', views.userList, name='user-list'),
    path('user-create', views.userCreate, name='user-create'),
    path('user-update/<int:id>', views.userUpdate, name='user-update'),
    path('user-delete/<int:id>', views.userDelete, name='user-delete')
]