from django.urls import path

from . import views


urlpatterns=[
     path('',views.home,name="home"),


     path('shop/<str:pk>/',views.shop,name="shop"),
     path('create-shop',views.createshop,name="create-shop"),
     path('update-shop/<str:pk>/',views.updateshop,name="update-shop"),
     path('delete-shop/<str:pk>/',views.deleteshop,name="delete-shop"),



     path('create-item/<str:pk>/',views.createitem,name="create-item"),
     path('update-item/<str:pk>/',views.updateitem,name="update-item"),
     path('delete-item/<str:pk>/',views.deleteitem,name="delete-item"),


     path('delete-message/<str:pk>/',views.deletemessage,name="delete-message"),

     path('login/',views.loginpage,name="login"),
     path('logout/',views.logoutpage,name="logout"),
     path('register/',views.registerpage,name="register"),


     path('rating/<str:pk>/',views.deleterating,name="delete-rating"),
     path('profile/<str:pk>/',views.profilepage,name="profile"),
     path('update-user/',views.updateuser,name="update-user"),

     path('comments/<str:pk>/',views.separateComments,name="comments"),


]


