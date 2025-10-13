from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from itertools import chain
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.


def HomePage(request):
    MainSlider = MainSliderModel.objects.all()
    BestMenu = BestMenuModel.objects.all()[:1]
    Menu = MenuModel.objects.all()[:1]
    About = AboutModel.objects.all()[:1]
    AboutItem = AboutItemModel.objects.all()
    Promotion = PromotionModel.objects.all()[:1]
    Strength = StrengthModel.objects.all()[:1]
    StrengthItem = StrengthItemModel.objects.all()[:1]
    Rate = RateModel.objects.all()
    DownloadAPP = DownloadAPPModel.objects.all()[:1]
    Chef = ChefModel.objects.all()[:1]
    ChefItem = ChefItemModel.objects.all()
    BookTable = BookTableModel.objects.all()[:1]
    DateTime = DateTimeModel.objects.all()
    BookTableOrderList = BookTableOrderListModel.objects.all()
    Feedback = FeedbackModel.objects.all()[:1]
    FeedbackItem = FeedbackItemModel.objects.all()
    Blog = BlogModel.objects.all()[:1]
    BlogItem = BlogItemModel.objects.all()
    Category = CategoryModel.objects.all()
    products = Product.objects.all()
    category1 = CategoryModel.objects.get(name='Beef Burger')
    products1 = Product.objects.filter(category=category1)
    category2 = CategoryModel.objects.get(name='Chicken Pizza')
    products2 = Product.objects.filter(category=category2)
    category3 = CategoryModel.objects.get(name='Hot Sushi')
    products3 = Product.objects.filter(category=category3)
    category4 = CategoryModel.objects.get(name='Drink & Juice')
    products4 = Product.objects.filter(category=category4)
    category5 = CategoryModel.objects.get(name='Fresh Pasta')
    products5 = Product.objects.filter(category=category5)
    category6 = CategoryModel.objects.get(name='Sea Food')
    products6 = Product.objects.filter(category=category6)
    Contact = ContactModel.objects.all()
    #

    #
    context = {
        'MainSlider': MainSlider,
        'BestMenu': BestMenu,
        'Menu': Menu,
        'About': About,
        'AboutItem': AboutItem,
        'Promotion': Promotion,
        'Strength': Strength,
        'StrengthItem': StrengthItem,
        'Rate': Rate,
        'DownloadAPP': DownloadAPP,
        'Chef': Chef,
        'ChefItem': ChefItem,
        'BookTable': BookTable,
        'DateTime': DateTime,
        'BookTableOrderList': BookTableOrderList,
        'Feedback': Feedback,
        'FeedbackItem': FeedbackItem,
        'Blog': Blog,
        'BlogItem': BlogItem,
        'Category': Category,
        'products': products,
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4,
        'products5': products5,
        'products6': products6,
        'Contact': Contact,
    }
    return render(request, 'index.html', context)


def MenuPage(request):
    MenuSlider = MenuSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Gallery = GalleryModel.objects.all()
    category1 = CategoryModel.objects.get(name='Beef Burger')
    products1 = Product.objects.filter(category=category1)
    category2 = CategoryModel.objects.get(name='Chicken Pizza')
    products2 = Product.objects.filter(category=category2)
    category3 = CategoryModel.objects.get(name='Hot Sushi')
    products3 = Product.objects.filter(category=category3)
    category4 = CategoryModel.objects.get(name='Drink & Juice')
    products4 = Product.objects.filter(category=category4)
    category5 = CategoryModel.objects.get(name='Fresh Pasta')
    products5 = Product.objects.filter(category=category5)
    category6 = CategoryModel.objects.get(name='Sea Food')
    products6 = Product.objects.filter(category=category6)
    context = {
        'MenuSlider': MenuSlider,
        'MenuCategory': MenuCategory,
        'Gallery': Gallery,
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4,
        'products5': products5,
        'products6': products6,
    }
    return render(request, 'menu.html', context)


def ShopPage(request):
    ShopSlider = ShopSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Gallery = GalleryModel.objects.all()
    products = Product.objects.all()
    default_product = Product.objects.first()
    context = {
        'ShopSlider': ShopSlider,
        'MenuCategory': MenuCategory,
        'Gallery': Gallery,
        'products': products,
        'default_product': default_product,
    }
    return render(request, 'shop.html', context)


def ShopDetailPage(request, pk):
    ShopDetailSlider = ShopDetailSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Gallery = GalleryModel.objects.all()
    FeedbackItem = FeedbackItemModel.objects.all()
    Description = DescriptionModel.objects.all()
    Product1 = ProductModel.objects.all()
    # single product object # Selected Product object
    product_obj = get_object_or_404(Product, pk=pk)
    # template loop အတွက် queryset လည်းလိုအပ်ရင်
    products = Product.objects.all()  # ဒီလို
    # Related ProductDetail objects (ManyToMany)
    product_details = ProductDetail.objects.select_related(
        'category').filter(product__id=product_obj.id)
    # Optional: first detail only
    product_detail = product_details.first() if product_details.exists() else None
    images = product_detail.images.all()  # related_name="images"
    context = {
        'ShopDetailSlider': ShopDetailSlider,
        'MenuCategory': MenuCategory,
        'Gallery': Gallery,
        'FeedbackItem': FeedbackItem,
        'Description': Description,
        'Product1': Product1,
        "products": products,  # loop လုပ်နိုင်အောင်
        "product_obj": product_obj,  # single product object detail page # Selected Product
        "product_details": product_details,  # Related ProductDetail list
        "product_detail": product_detail,  # Single ProductDetail
        "images": images,
    }
    return render(request, 'shop_detail.html', context)


def NewPage(request):
    NewSlider = NewSliderModel.objects.all()
    New = NewModel.objects.all()
    tag = Tag.objects.all()
    Profile = ProfileModel.objects.all()
    Post = PostModel.objects.all()
    Gallery = GalleryModel.objects.all()

    context = {
        'NewSlider': NewSlider,
        'New': New,
        'tag': tag,
        'Profile': Profile,
        'Gallery': Gallery,
        'Post': Post,
    }
    return render(request, 'new.html', context)


def NewDetailPage(request):
    NewDetailSlider = NewDetailSliderModel.objects.all()
    NewDetailTag = NewDetailTagModel.objects.all()
    NewDetail = NewDetailModel.objects.all()
    Comment = CommentModel.objects.all()
    CommentCount = CommentModel.objects.all().count()
    tag = Tag.objects.all()
    Profile = ProfileModel.objects.all()
    Post = PostModel.objects.all()
    Gallery = GalleryModel.objects.all()
    context = {
        'NewDetailSlider': NewDetailSlider,
        'NewDetailTag': NewDetailTag,
        'NewDetail': NewDetail,
        'Comment': Comment,
        'CommentCount': CommentCount,
        'tag': tag,
        'Profile': Profile,
        'Gallery': Gallery,
        'Post': Post,
    }
    return render(request, 'newDetail.html', context)


def ContactPage(request):
    ContactSlider = ContactSliderModel.objects.all()
    Contact = ContactModel.objects.all()
    Gallery = GalleryModel.objects.all()
    context = {
        'ContactSlider': ContactSlider,
        'Gallery': Gallery,
        'Contact': Contact,
    }
    return render(request, 'contact.html', context)


def AboutPage(request):
    AboutSlider = AboutSliderModel.objects.all()[:1]
    AboutFeedback = AboutFeedbackModel.objects.all()
    AboutExperience = AboutExperienceModel.objects.all()
    AboutService = AboutServiceModel.objects.all()
    AboutUs = AboutUsModel.objects.all()
    AboutUsItem = AboutUsItemModel.objects.all()
    Gallery = GalleryModel.objects.all()
    Chef = ChefModel.objects.all()[:1]
    ChefItem = ChefItemModel.objects.all()
    FeedbackItem = FeedbackItemModel.objects.all()
    context = {
        'AboutSlider': AboutSlider,
        'AboutFeedback': AboutFeedback,
        'AboutService': AboutService,
        'AboutExperience': AboutExperience,
        'AboutUs': AboutUs,
        'AboutUsItem': AboutUsItem,
        'Gallery': Gallery,
        'Chef': Chef,
        'ChefItem': ChefItem,
        'FeedbackItem': FeedbackItem,
    }
    return render(request, 'about.html', context)


def CartPage(request):
    CartSlider = CartSliderModel.objects.all()[:1]
    Gallery = GalleryModel.objects.all()
    context = {
        'CartSlider': CartSlider,
        'Gallery': Gallery,
    }
    return render(request, 'cart.html', context)


@login_required
def WishListPage(request):
    WishListSlider = WishListSliderModel.objects.all()[:1]
    Gallery = GalleryModel.objects.all()
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    context = {
        'WishListSlider': WishListSlider,
        'Gallery': Gallery,
        'wishlist': wishlist,
    }
    return render(request, 'wishList.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist_view')


def CheckOutPage(request):
    CheckOutSlider = CheckOutSliderModel.objects.all()[:1]
    Gallery = GalleryModel.objects.all()
    context = {
        'CheckOutSlider': CheckOutSlider,
        'Gallery': Gallery,
    }
    return render(request, 'checkOut.html', context)


def LoginPage(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, email=email, password=password)
    if user is not None:
        login(request, user)
        messages.success(request,"You are now logged in as " + username|email)
        return redirect('')
    else:
        messages.error(request, "Username or email or Password is incorrect!")

    return render(request, 'login.html')

@login_required(login_url='loginPage')
def dashboard(request):
    return render(request, 'admin_dashboard.html')

# @permission_required('myapp.change_product', raise_exception=True)
# def edit_product(request):

def dashboard(request):
    if request.user.role == 'admin':
        # show admin content
        ...
    else:
        return redirect('homePage')


def Logout(request):  
    logout(request) 
    messages.success(request, "You are now logout! ") 
    return redirect('login')  

def RegisterPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('')  # Redirect to login page after registration
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
