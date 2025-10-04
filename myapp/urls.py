from django.urls import path 
from .import views

urlpatterns = [
    path('',views.HomePage,name="homePage"),
    path('menu/',views.MenuPage,name="menuPage"),
    path('shop/',views.ShopPage,name="shopPage"),
    path('shopDetail/',views.ShopDetailPage,name="shopDetailPage"),
    path('new/',views.NewPage,name="newPage"),
    path('newDetail/',views.NewDetailPage,name="newDetailPage"),
    path('contact/',views.ContactPage,name="contactPage"),
    path('about/',views.AboutPage,name="aboutPage"),
]