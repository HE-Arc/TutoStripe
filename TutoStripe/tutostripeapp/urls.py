from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tutostripeapp-home'),
    path('simple-buy/', views.simple_buy, name='simple-buy'),
    path('different-buy/', views.different_buy, name='different-buy'),
]