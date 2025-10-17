from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def CategoryList(request):
    category = CategoryModel.objects.all()
    context = {
        'category' : category
    }
    return render(request,'Category/categoryList.html',context)

def CategoryCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        num = request.POST.get('num')
        image = request.POST.get('image')

        CategoryModel.objects.create(
            name = name,
            num = num,
            image = image,
        )
        return redirect('categoryList')
    return render(request,'Category/categoryCreate.html')

def CategoryUpdate(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)

    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.num = request.POST.get('num')

        if 'image' in request.FILES:
            category.image = request.FILES['image']

        category.save()
        return redirect('CategoryList')

    return render(request, 'Category/categoryUpdate.html', {'category': category})

def CategoryDetail(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    return render(request,'Category/categoryDetail.html',{ 'category': category })

def CategoryDelete(request,pk):
    category = get_object_or_404(CategoryModel, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('CategoryList')

    return render(request,'Category/categoryList.html',{ 'category': category })

def CategoryList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        category = CategoryModel.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        category = CategoryModel.objects.all().order_by('-updated_at')
    else:  # newest
        category = CategoryModel.objects.all().order_by('-created_at')

    context = {
        'category': category,
        'sort_by': sort_by
    }
    return render(request,'Category/categoryList.html',context)