from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from itertools import chain
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, ValidationError


User = get_user_model()
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
    BookTable = BookTableModel.objects.all()
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

    # Get or create wishlist for this user
    wishlist = Wishlist.objects.filter(user=request.user).first()
    products = wishlist.products.all() if wishlist else []

    context = {
        'WishListSlider': WishListSlider,
        'Gallery': Gallery,
        'wishlist': wishlist,
        'products': products,
    }
    return render(request, 'wishList.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('WishListPage')

@login_required
def remove_from_wishlist(request, product_id):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    wishlist.products.remove(product)
    
    # Optional: wishlist empty ဖြစ်ရင် delete လုပ်နိုင်
    if wishlist.products.count() == 0:
        wishlist.delete()
    
    return redirect('WishListPage')


def CheckOutPage(request):
    CheckOutSlider = CheckOutSliderModel.objects.all()[:1]
    Gallery = GalleryModel.objects.all()
    context = {
        'CheckOutSlider': CheckOutSlider,
        'Gallery': Gallery,
    }
    return render(request, 'checkOut.html', context)

@login_required
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.total_price() for item in cart_items)
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('loginPage')  # change this to your login URL name

    # Get or create a cart item for this user & product
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cartPage')

@login_required
def remove_from_cart(request, cart_item_id):
    item = CartItem.objects.get(id=cart_item_id)
    item.delete()
    return redirect('cartPage')

def update_cart_quantity(request, cart_item_id, action):
    item = get_object_or_404(CartItem, id=cart_item_id)
    if action == "increase":
        item.quantity += 1
    elif action == "decrease" and item.quantity > 1:
        item.quantity -= 1
    item.save()
    return redirect('cartPage')

def LoginPage(request):
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')  # username or email field
        password = request.POST.get('password')

        user = None

        # Try to find by username first
        try:
            user_obj = CustomUser.objects.get(username=identifier)
            user = authenticate(request, username=user_obj.username, password=password)
        except CustomUser.DoesNotExist:
            # Try by email if username not found
            try:
                user_obj = CustomUser.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except CustomUser.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('homePage')  # Change this to your homepage URL name
        else:
            messages.error(request, "Invalid username/email or password.")

    return render(request, 'login.html')

@login_required
def move_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Add to cart
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Remove from wishlist
    Wishlist.objects.filter(user=request.user, products=product).delete()

    messages.success(request, f"{product.title} moved to your cart.")
    return redirect('cartPage')

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
    return redirect('/login/') 

def RegisterPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check required fields
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'register.html')

        # Validate password with Django validators
        try:
            validate_password(password)
        except ValidationError as e:
            # e is a list of error messages
            for msg in e:
                messages.error(request, msg)
            return render(request, 'register.html')

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'register.html')

        # Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        messages.success(request, f"Welcome {username}! Your account has been created successfully.")
        return redirect('homePage') 

    return render(request, 'register.html')
