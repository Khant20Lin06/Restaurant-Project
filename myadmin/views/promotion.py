from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def PromotionList(request):
    promotion = PromotionModel.objects.all()
    context = {
        'promotion' : promotion
    }
    return render(request,'HomePage/4_Promotion/promotionList.html',context)

def PromotionCreate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        disPrice = request.POST.get('disPrice')
        image = request.POST.get('image')
        start_date = request.POST.get('start_date')
        duration_days = request.POST.get('duration_days')
        is_active = request.POST.get('is_active')

        PromotionModel.objects.create(
            title = title,
            description = description,
            price = price,
            disPrice = disPrice,
            start_date = start_date,
            image = image,
            duration_days = duration_days,
            is_active = is_active,
        )
        return redirect('PromotionList')
    return render(request,'HomePage/4_Promotion/PromotionCreate.html')

def PromotionUpdate(request, pk):
    promotion = get_object_or_404(PromotionModel, pk=pk)

    if request.method == 'POST':
        promotion.title = request.POST.get('title')
        promotion.description = request.POST.get('description')
        promotion.price = request.POST.get('price')
        promotion.disPrice = request.POST.get('disPrice')
        promotion.start_date = request.POST.get('start_date')
        promotion.duration_days = request.POST.get('duration_days')
        promotion.is_active = request.POST.get('is_active')

        if 'image' in request.FILES:
            promotion.image = request.FILES['image']

        promotion.save()
        return redirect('PromotionList')

    return render(request, 'HomePage/4_Promotion/PromotionUpdate.html', {'promotion': promotion})

def PromotionDetail(request, pk):
    promotion = get_object_or_404(PromotionModel, pk=pk)
    return render(request,'HomePage/4_Promotion/PromotionDetail.html',{ 'promotion': promotion })

def PromotionDelete(request,pk):
    promotion = get_object_or_404(PromotionModel, pk=pk)

    if request.method == 'POST':
        promotion.delete()
        return redirect('PromotionList')

    return render(request,'HomePage/4_Promotion/PromotionList.html',{ 'promotion': promotion })

def PromotionList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        promotion = PromotionModel.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        promotion = PromotionModel.objects.all().order_by('-updated_at')
    else:  # newest
        promotion = PromotionModel.objects.all().order_by('-created_at')

    context = {
        'promotion': promotion,
        'sort_by': sort_by
    }
    return render(request,'HomePage/4_Promotion/PromotionList.html',context)