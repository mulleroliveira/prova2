from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listagem/', views.users),
    path('listagem/delete/<int:id>/', views.delete)
]
