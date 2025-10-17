from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def MainSliderList(request):
    mainSlider = MainSliderModel.objects.all()
    context = {
        'mainSlider' : mainSlider
    }
    return render(request,'HomePage/1_MainSlider/mainsliderlist.html',context)

def MainSliderCreate(request):
    if request.method == 'POST':
        into1 = request.POST.get('into1')
        into2 = request.POST.get('into2')
        into3 = request.POST.get('into3')
        into4 = request.POST.get('into4')
        order = request.POST.get('order')
        menu = request.POST.get('menu')
        num = request.POST.get('num')
        bgImage = request.POST.get('bgImage')

        MainSliderModel.objects.create(
            into1 = into1,
            into2 = into2,
            into3 = into3,
            into4 = into4,
            order = order,
            menu = menu,
            num = num,
            bgImage = bgImage,
        )
        return redirect('MainSliderList')
    return render(request,'HomePage/1_MainSlider/mainslidercreate.html')

def MainSliderUpdate(request, pk):
    mainSlider = get_object_or_404(MainSliderModel, pk=pk)

    if request.method == 'POST':
        mainSlider.into1 = request.POST.get('into1')
        mainSlider.into2 = request.POST.get('into2')
        mainSlider.into3 = request.POST.get('into3')
        mainSlider.into4 = request.POST.get('into4')
        mainSlider.order = request.POST.get('order')
        mainSlider.menu = request.POST.get('menu')
        mainSlider.num = request.POST.get('num')

        # ✅ Handle file upload correctly
        if 'bgImage' in request.FILES:
            mainSlider.bgImage = request.FILES['bgImage']

        mainSlider.save()
        return redirect('MainSliderList')

    return render(request, 'HomePage/1_MainSlider/mainsliderupdate.html', {'mainSlider': mainSlider})
    # return render(request,'mainsliderupdate.html')

def MainSliderDetail(request, pk):
    mainSlider = get_object_or_404(MainSliderModel, pk=pk)
    return render(request,'HomePage/1_MainSlider/mainsliderdetail.html',{ 'mainSlider': mainSlider })
    # return render(request,'mainsliderdetail.html')

def MainSliderDelete(request,pk):
    mainSlider = get_object_or_404(MainSliderModel, pk=pk)

    if request.method == 'POST':
        mainSlider.delete()
        return redirect('MainSliderList')

    return render(request,'HomePage/1_MainSlider/mainsliderlist.html',{ 'mainSlider': mainSlider })
    # return render(request,'mainsliderlist.html')

def MainSliderList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        mainSlider = MainSliderModel.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        mainSlider = MainSliderModel.objects.all().order_by('-updated_at')
    else:  # newest
        mainSlider = MainSliderModel.objects.all().order_by('-created_at')

    context = {
        'mainSlider': mainSlider,
        'sort_by': sort_by
    }
    return render(request,'HomePage/1_MainSlider/mainsliderList.html',context)