from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def AdminDashboard(request):
    mainslider_count = MainSliderModel.objects.all().count()

    context = {
        'mainslider_count' : mainslider_count,
    }

    return render(request,'admin_dashboard.html',context)