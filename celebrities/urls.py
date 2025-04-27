from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('celebrity/<int:celebrity_id>/', views.detail, name='celebrity_detail'),
]
