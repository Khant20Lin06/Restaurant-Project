from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
# Create your views here.

def ProductDetailList(request):
    productDetail = ProductDetail.objects.all()
    context = {
        'productDetail' : productDetail
    }
    return render(request,'ProductDetail/productDetailList.html',context)

def ProductDetailCreate(request):
    categories = CategoryModel.objects.all() 
    products = Product.objects.all() 
    tags = Tag.objects.all() 
    images = ProductImageModel.objects.all() 

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        disPrice = request.POST.get('disPrice')
        sku = request.POST.get('sku')
        category_id = request.POST.get('category') 
        product_id = request.POST.get('product') 
        tag_id = request.POST.get('tag') 

        if not category_id or not product_id or not tag_id:
            return render(request, 'ProductDetail/productDetailCreate.html', {
                'categories': categories,
                'products': products,
                'tags': tags,
                'images': images,
                'error': "Please select category, product, and tag before submitting.",
            })

        category = get_object_or_404(CategoryModel, id=category_id)
        product = get_object_or_404(Product, id=product_id)
        tag = get_object_or_404(Tag, id=tag_id)

        product_detail = ProductDetail.objects.create(
            title = title,
            disPrice = disPrice,
            price = price,
            SKU = sku,
            description = description,
            category = category,
            product = product,
            tag = tag,
        )

        if 'image' in request.FILES:
            image_file = request.FILES['image']
            ProductImageModel.objects.create(product=product_detail, image=image_file)

        return redirect('ProductDetailList')
    context = {
        'categories': categories,
        'products': products,
        'tags': tags,
        'images': images,
        }
    return render(request,'ProductDetail/productDetailCreate.html',context)

def ProductDetailUpdate(request, pk):
    productDetail = get_object_or_404(ProductDetail, pk=pk)
    categories = CategoryModel.objects.all() 
    products = Product.objects.all() 
    tags = Tag.objects.all() 
    images = ProductImageModel.objects.all() 

    if request.method == 'POST':
        productDetail.title = request.POST.get('title')
        productDetail.description = request.POST.get('description')
        productDetail.price = request.POST.get('price')
        productDetail.disPrice = request.POST.get('disPrice')
        productDetail.SKU = request.POST.get('sku')
        
        category_id = request.POST.get('category')
        product_id = request.POST.get('product')
        tag_id = request.POST.get('tag')
        productDetail.category = get_object_or_404(CategoryModel, id=category_id)
        productDetail.product = get_object_or_404(Product, id=product_id)
        productDetail.tag = get_object_or_404(Tag, id=tag_id)

        if 'image' in request.FILES:
            image_file = request.FILES['image']
            ProductImageModel.objects.create(product=productDetail, image=image_file)

        productDetail.save()
        return redirect('ProductDetailList')

    return render(request, 'ProductDetail/productDetailUpdate.html', {
        'productDetail': productDetail,
        'categories': categories,
        'products': products,
        'tags': tags,
        'images': images,
    })

def ProductDetailDetail(request, pk):
    productDetail = get_object_or_404(ProductDetail, pk=pk)
    return render(request,'ProductDetail/productDetailDetail.html',{ 'productDetail': productDetail })

def ProductDetailDelete(request,pk):
    productDetail = get_object_or_404(ProductDetail, pk=pk)

    if request.method == 'POST':
        productDetail.delete()
        return redirect('ProductDetailList')

    return render(request,'ProductDetail/productDetailList.html',{ 'productDetail': productDetail })

def ProductDetailList(request):
    sort_by = request.GET.get('sort', 'newest')  # default newest

    if sort_by == 'oldest':
        productDetail = ProductDetail.objects.all().order_by('created_at')
    elif sort_by == 'recent':
        productDetail = ProductDetail.objects.all().order_by('-updated_at')
    else:  # newest
        productDetail = ProductDetail.objects.all().order_by('-created_at')

    context = {
        'productDetail': productDetail,
        'sort_by': sort_by
    }
    return render(request,'ProductDetail/productDetailList.html',context)