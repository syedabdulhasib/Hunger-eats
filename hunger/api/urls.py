from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('shops/',views.getShops),
    path('shops/items/',views.getShopsItems),
    path('shops/<str:pk>',views.getShop),
    path('shops/<str:pk>/items/',views.getShopItems)
]