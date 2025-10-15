from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.HomePage, name="homePage"),
    path('menu/', views.MenuPage, name="menuPage"),
    path('shop/', views.ShopPage, name="shopPage"),
    path('shopDetail/<uuid:pk>/', views.ShopDetailPage, name='shopDetailPage'),
    path('new/', views.NewPage, name="newPage"),
    path('newDetail/', views.NewDetailPage, name="newDetailPage"),
    path('contact/', views.ContactPage, name="contactPage"),
    path('about/', views.AboutPage, name="aboutPage"),
    path('cart/', views.CartPage, name="CartPage"),
    path('cart/', views.cart_page, name='cartPage'),
    path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<uuid:cart_item_id>/',views.remove_from_cart, name='removeFromCart'),
    path('cart/update/<uuid:cart_item_id>/<str:action>/',views.update_cart_quantity, name='updateCart'),
    path('wishlist/move/<uuid:product_id>/', views.move_to_cart, name='move_to_cart'),
    path('wishlist/', views.WishListPage, name='WishListPage'),
    path('wishlist/add/<uuid:product_id>/',views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<uuid:product_id>/',views.remove_from_wishlist, name='remove_from_wishlist'),
    path('checkOut/', views.CheckOutPage, name="checkOutPage"),
    path('login/', views.LoginPage, name='loginPage'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.RegisterPage, name="registerPage"),
]
