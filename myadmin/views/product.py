from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def ProductList(request):
    product = Product.objects.all()
    context = {
        'product' : product
    }
    return render(request,'Product/productList.html',context)

def ProductCreate(request):
    categories = CategoryModel.objects.all() 
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        price = request.POST.get('price')
        disPrice = request.POST.get('disPrice')
        category_id = request.POST.get('category') 
        image = request.POST.get('image')

        category = get_object_or_404(CategoryModel, id=category_id)

        Product.objects.create(
            title = title,
            disPrice = disPrice,
            price = price,
            text = text,
            category = category,
            image = image,
        )
        return redirect('ProductList')
    context = {'categories': categories}
    return render(request,'Product/productCreate.html',context)

def ProductUpdate(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = CategoryModel.objects.all() 

    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.text = request.POST.get('text')
        product.price = request.POST.get('price')
        product.disPrice = request.POST.get('disPrice')
        
        category_id = request.POST.get('category')
        product.category = get_object_or_404(CategoryModel, id=category_id)

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        return redirect('ProductList')

    return render(request, 'Product/productUpdate.html', {
        'product': product,
        'categories': categories
    })

def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,'Product/productDetail.html',{ 'product': product })

def ProductDelete(request,pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('ProductList')

    return render(request,'Product/productList.html',{ 'product': product })

def ProductList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        product = Product.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        product = Product.objects.all().order_by('-updated_at')
    else:  # newest
        product = Product.objects.all().order_by('-created_at')

    context = {
        'product': product,
        'sort_by': sort_by
    }
    return render(request,'Product/productList.html',context)