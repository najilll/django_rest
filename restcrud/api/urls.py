from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('api/items/<int:pk>/edit/', views.editItem, name='edit_item'),
    path('api/items/<int:pk>/delete/', views.deleteItem, name='delete_item'),
]
