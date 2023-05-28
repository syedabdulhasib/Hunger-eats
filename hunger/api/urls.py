from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('shops/',views.getShops),
    path('shops/<str:pk>',views.getShop),
]