from django.urls import path 
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.HomePage,name="homePage"),
    path('menu/',views.MenuPage,name="menuPage"),
    path('shop/',views.ShopPage,name="shopPage"),
    path('shopDetail/<uuid:pk>/', views.ShopDetailPage, name='shopDetailPage'),
    path('new/',views.NewPage,name="newPage"),
    path('newDetail/',views.NewDetailPage,name="newDetailPage"),
    path('contact/',views.ContactPage,name="contactPage"),
    path('about/',views.AboutPage,name="aboutPage"),
    path('wishlist/add/<uuid:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('cart/',views.CartPage,name="cartPage"),
    path('wishList/',views.WishListPage,name="wishListPage"),
    path('checkOut/',views.CheckOutPage,name="checkOutPage"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='loginPage'),
    path('logout/', auth_views.LogoutView.as_view(next_page='loginPage'), name='logout'),
    path('register/',views.RegisterPage,name="registerPage"),
]