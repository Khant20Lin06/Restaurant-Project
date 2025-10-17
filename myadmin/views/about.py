from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def AboutList(request):
    about = AboutModel.objects.all()
    context = {
        'about' : about
    }
    return render(request,'HomePage/2_About/aboutList.html',context)

def AboutCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        tag = request.POST.get('tag')
        into = request.POST.get('into')
        pName = request.POST.get('pName')
        position = request.POST.get('position')
        year = request.POST.get('year')
        company = request.POST.get('company')
        image = request.POST.get('image')
        pImage = request.POST.get('pImage')

        AboutModel.objects.create(
            name = name,
            description = description,
            tag = tag,
            into = into,
            pName = pName,
            position = position,
            year = year,
            company = company,
            image = image,
            pImage = pImage,
        )
        return redirect('AboutList')
    return render(request,'HomePage/2_About/aboutCreate.html')

def AboutUpdate(request, pk):
    about = get_object_or_404(AboutModel, pk=pk)

    if request.method == 'POST':
        about.name = request.POST.get('name')
        about.description = request.POST.get('description')
        about.tag = request.POST.get('tag')
        about.into = request.POST.get('into')
        about.pName = request.POST.get('pName')
        about.position = request.POST.get('position')
        about.year = request.POST.get('year')
        about.company = request.POST.get('company')

        if 'image' in request.FILES:
            about.image = request.FILES['image']

        if 'pImage' in request.FILES:
            about.pImage = request.FILES['pImage']

        about.save()
        return redirect('AboutList')

    return render(request, 'HomePage/2_About/aboutUpdate.html', {'about': about})

def AboutDetail(request, pk):
    about = get_object_or_404(AboutModel, pk=pk)
    return render(request,'HomePage/2_About/aboutDetail.html',{ 'about': about })

def AboutDelete(request,pk):
    about = get_object_or_404(AboutModel, pk=pk)

    if request.method == 'POST':
        about.delete()
        return redirect('AboutList')

    return render(request,'HomePage/2_About/aboutList.html',{ 'about': about })

def AboutList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        about = AboutModel.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        about = AboutModel.objects.all().order_by('-updated_at')
    else:  # newest
        about = AboutModel.objects.all().order_by('-created_at')

    context = {
        'about': about,
        'sort_by': sort_by
    }
    return render(request,'HomePage/2_About/aboutList.html',context)