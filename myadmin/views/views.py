from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def AdminDashboard(request):
    mainslider_count = MainSliderModel.objects.all().count()
    data = [
        {
            "name": "BookATables",
            "count": BookATable.objects.count(),
            "icon": "utensils",
            "colorclass":"std-data",
        },
        {
            "name": "Orders",
            "count": Order.objects.count(),
            "icon": "shopping-cart",
            "colorclass":"teach-data",
        },
        {
            "name": "User",
            "count": CustomUser.objects.count(),
            "icon": "users",
            "colorclass":"event-data",
        },
        {
            "name": "Product",
            "count": Product.objects.count(),
            "icon": "hamburger",
            "colorclass":"food-data",
        },
    ]

    context = {
        'mainslider_count' : mainslider_count,
        "dashboard_data": data
    }

    return render(request,'admin_dashboard.html',context)

def dashboard_view(request):
    data = [
        {
            "name": "BookATables",
            "count": BookATable.objects.count(),
            "icon": "user-graduate"
        },
        {
            "name": "Orders",
            "count": Order.objects.count(),
            "icon": "chalkboard-teacher"
        },
        {
            "name": "User",
            "count": User.objects.count(),
            "icon": "calendar-alt"
        },
        {
            "name": "Product",
            "count": Product.objects.count(),
            "icon": "hamburger"
        },
    ]
    return render(request, "admin_dashboard.html", {"dashboard_data": data})