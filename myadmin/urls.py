from django.urls import path 
from .views import views,mainSlider

urlpatterns = [
    path('', views.AdminDashboard, name="admin_dashboard"),
    path('mainsliderlist/', mainSlider.MainSliderList, name="MainSliderList"),
    path('mainslidercreate/', mainSlider.MainSliderCreate, name="MainSliderCreate"),
    path('mainsliderupdate/update/<uuid:pk>/', mainSlider.MainSliderUpdate, name="MainSliderUpdate"),
    path('mainsliderdetail/detail/<uuid:pk>/', mainSlider.MainSliderDetail, name="MainSliderDetail"),
    path('mainsliderdelete/delete/<uuid:pk>/', mainSlider.MainSliderDelete, name="MainSliderDelete"),
]