from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.food, name='form'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),

]