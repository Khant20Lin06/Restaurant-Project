from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def OrderList(request):
    orders = OrderItem.objects.all()
    context = {
        'orders' : orders
    }
    return render(request,'Order/orderList.html',context)

def OrderDelete(request,pk):
    orders = get_object_or_404(OrderItem, pk=pk)

    if request.method == 'POST':
        orders.delete()
        return redirect('OrderList')

    return render(request,'Order/orderList.html',{ 'orders' : orders })

def OrderList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        orders = OrderItem.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        orders = OrderItem.objects.all().order_by('-updated_at')
    else:  # newest
        orders = OrderItem.objects.all().order_by('-created_at')

    context = {
        'orders' : orders,
        'sort_by': sort_by
    }
    return render(request,'Order/OrderList.html',context)