from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/<str:coin_id>/', views.coin_detail, name='coin_detail'),
]
