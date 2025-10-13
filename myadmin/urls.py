from django.urls import path 
from .import views

urlpatterns = [
    path('', views.AdminDashboard, name="admin_dashboard"),
]