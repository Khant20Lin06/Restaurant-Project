from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def AboutItemList(request):
    aboutItem = AboutItemModel.objects.all()
    context = {
        'aboutItem' : aboutItem
    }
    return render(request,'HomePage/3_AboutItem/aboutItemList.html',context)

def AboutItemCreate(request):
    if request.method == 'POST':
        text = request.POST.get('text')

        AboutItemModel.objects.create(
            text = text,
        )
        return redirect('AboutItemList')
    return render(request,'HomePage/3_AboutItem/aboutItemCreate.html')

def AboutItemUpdate(request, pk):
    aboutItem = get_object_or_404(AboutItemModel, pk=pk)

    if request.method == 'POST':
        aboutItem.text = request.POST.get('text')

        aboutItem.save()
        return redirect('AboutItemList')

    return render(request, 'HomePage/3_AboutItem/aboutItemUpdate.html', {'aboutItem': aboutItem})

def AboutItemDetail(request, pk):
    aboutItem = get_object_or_404(AboutItemModel, pk=pk)
    return render(request,'HomePage/3_AboutItem/aboutItemDetail.html',{ 'aboutItem': aboutItem })

def AboutItemDelete(request,pk):
    aboutItem = get_object_or_404(AboutItemModel, pk=pk)

    if request.method == 'POST':
        aboutItem.delete()
        return redirect('AboutItemList')

    return render(request,'HomePage/3_AboutItem/aboutItemList.html',{ 'aboutItem': aboutItem })

def AboutItemList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        aboutItem = AboutItemModel.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        aboutItem = AboutItemModel.objects.all().order_by('-updated_at')
    else:  # newest
        aboutItem = AboutItemModel.objects.all().order_by('-created_at')

    context = {
        'aboutItem': aboutItem,
        'sort_by': sort_by
    }
    return render(request,'HomePage/3_AboutItem/aboutItemList.html',context)