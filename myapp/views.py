from django.shortcuts import render
from .models import *
from itertools import chain

# Create your views here.

def HomePage(request):
    MainSlider = MainSliderModel.objects.all()
    BestMenu = BestMenuModel.objects.all()[:1]
    Menu = MenuModel.objects.all()[:1]
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category4 = Category4Model.objects.all()
    Category44 = Category44Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
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
    # 
    categories = list(chain(Category1, Category11, Category2, Category22, Category3, Category33, Category4, Category44, Category5, Category55, Category6, Category66))
    # 
    context = {
        'MainSlider' : MainSlider,
        'BestMenu' : BestMenu,
        'Menu' : Menu,
        'Category1' : Category1,
        'Category11' : Category11,
        'Category2' : Category2,
        'Category22' : Category22,
        'Category3' : Category3,
        'Category33' : Category33,
        'Category4' : Category4,
        'Category44' : Category44,
        'Category5' : Category5,
        'Category55' : Category55,
        'Category6' : Category6,
        'Category66' : Category66,
        'About' : About,
        'AboutItem' : AboutItem,
        'Promotion' : Promotion,
        'Strength' : Strength,
        'StrengthItem' : StrengthItem,
        'Rate' : Rate,
        'DownloadAPP' : DownloadAPP,
        'Chef' : Chef,
        'ChefItem' : ChefItem,
        'BookTable' : BookTable,
        'DateTime' : DateTime,
        'BookTableOrderList' : BookTableOrderList,
        'Feedback' : Feedback,
        'FeedbackItem' : FeedbackItem,
        'Blog' : Blog,
        'BlogItem' : BlogItem,
        'categories' : categories,
    }
    return render(request,'index.html',context)

def MenuPage(request):
    MenuSlider = MenuSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category4 = Category4Model.objects.all()
    Category44 = Category44Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
    Gallery = GalleryModel.objects.all()
    context = {
        'MenuSlider' : MenuSlider,
        'MenuCategory' : MenuCategory,
        'Category1' : Category1,
        'Category11' : Category11,
        'Category2' : Category2,
        'Category22' : Category22,
        'Category3' : Category3,
        'Category33' : Category33,
        'Category4' : Category4,
        'Category44' : Category44,
        'Category5' : Category5,
        'Category55' : Category55,
        'Category6' : Category6,
        'Category66' : Category66,
        'Gallery' : Gallery,
    }
    return render(request,'menu.html',context)


def ShopPage(request):
    ShopSlider = ShopSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category4 = Category4Model.objects.all()
    Category44 = Category44Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
    Gallery = GalleryModel.objects.all()
    # 
    categories = list(chain(Category1, Category11, Category2, Category22, Category3, Category33, Category4, Category44, Category5, Category55, Category6, Category66))
    # 
    context = {
        'ShopSlider' : ShopSlider,
        'MenuCategory' : MenuCategory,
        'Category1' : Category1,
        'Category11' : Category11,
        'Category2' : Category2,
        'Category22' : Category22,
        'Category3' : Category3,
        'Category33' : Category33,
        'Category4' : Category4,
        'Category44' : Category44,
        'Category5' : Category5,
        'Category55' : Category55,
        'Category6' : Category6,
        'Category66' : Category66,
        'Gallery' : Gallery,
        'categories' : categories,
    }
    return render(request,'shop.html',context)

def ShopDetailPage(request):
    ShopDetailSlider = ShopDetailSliderModel.objects.all()
    MenuCategory = MenuCategoryModel.objects.all()
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category4 = Category4Model.objects.all()
    Category44 = Category44Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
    Gallery = GalleryModel.objects.all()
    FeedbackItem = FeedbackItemModel.objects.all()
    Description = DescriptionModel.objects.all()
    Product = ProductModel.objects.all()
    # 
    categories = list(chain(Category1, Category11, Category2, Category22, Category3, Category33, Category4, Category44, Category5, Category55, Category6, Category66))
    # 
    context = {
        'ShopDetailSlider' : ShopDetailSlider,
        'MenuCategory' : MenuCategory,
        'Category1' : Category1,
        'Category11' : Category11,
        'Category2' : Category2,
        'Category22' : Category22,
        'Category3' : Category3,
        'Category33' : Category33,
        'Category4' : Category4,
        'Category44' : Category44,
        'Category5' : Category5,
        'Category55' : Category55,
        'Category6' : Category6,
        'Category66' : Category66,
        'Gallery' : Gallery,
        'FeedbackItem' : FeedbackItem,
        'Description' : Description,
        'Product' : Product,
        'categories' : categories,
    }
    return render(request,'shop_detail.html',context)

def NewPage(request):
    NewSlider = NewSliderModel.objects.all()
    New = NewModel.objects.all()
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
    Tag = TagModel.objects.all()
    Profile = ProfileModel.objects.all()
    Post = PostModel.objects.all()
    categoriesCount1 = list(chain(Category1, Category11))
    categoriesCount2 = list(chain(Category2, Category22))
    categoriesCount3 = list(chain(Category3, Category33))
    categoriesCount5 = list(chain(Category5, Category55))
    categoriesCount6 = list(chain(Category6, Category66))
    categories1 = len(categoriesCount1)
    categories2 = len(categoriesCount2)
    categories3 = len(categoriesCount3)
    categories5 = len(categoriesCount5)
    categories6 = len(categoriesCount6)

    context = {
        'NewSlider' : NewSlider,
        'New' : New,
        'Tag' : Tag,
        'Profile' : Profile,
        'Post' : Post,
        'categories1' : categories1,
        'categories2' : categories2,
        'categories3' : categories3,
        'categories5' : categories5,
        'categories6' : categories6,
        }
    return render(request,'new.html',context)

def NewDetailPage(request):
    NewDetailSlider = NewDetailSliderModel.objects.all()
    NewDetailTag = NewDetailTagModel.objects.all()
    NewDetail = NewDetailModel.objects.all()
    Comment = CommentModel.objects.all()
    CommentCount = CommentModel.objects.all().count()
    Category1 = Category1Model.objects.all()
    Category11 = Category11Model.objects.all()
    Category2 = Category2Model.objects.all()
    Category22 = Category22Model.objects.all()
    Category3 = Category3Model.objects.all()
    Category33 = Category33Model.objects.all()
    Category5 = Category5Model.objects.all()
    Category55 = Category55Model.objects.all()
    Category6 = Category6Model.objects.all()
    Category66 = Category66Model.objects.all()
    Tag = TagModel.objects.all()
    Profile = ProfileModel.objects.all()
    Post = PostModel.objects.all()
    categoriesCount1 = list(chain(Category1, Category11))
    categoriesCount2 = list(chain(Category2, Category22))
    categoriesCount3 = list(chain(Category3, Category33))
    categoriesCount5 = list(chain(Category5, Category55))
    categoriesCount6 = list(chain(Category6, Category66))
    categories1 = len(categoriesCount1)
    categories2 = len(categoriesCount2)
    categories3 = len(categoriesCount3)
    categories5 = len(categoriesCount5)
    categories6 = len(categoriesCount6)
    context = {
        'NewDetailSlider' : NewDetailSlider,
        'NewDetailTag' : NewDetailTag,
        'NewDetail' : NewDetail,
        'Comment' : Comment,
        'CommentCount' : CommentCount,
        'Tag' : Tag,
        'Profile' : Profile,
        'Post' : Post,
        'categories1' : categories1,
        'categories2' : categories2,
        'categories3' : categories3,
        'categories5' : categories5,
        'categories6' : categories6,
        }
    return render(request,'newDetail.html',context)

def ContactPage(request):
    ContactSlider = ContactSliderModel.objects.all()
    Contact = ContactModel.objects.all()
    context = {
        'ContactSlider' : ContactSlider,
        'Contact' : Contact,
        }
    return render(request,'contact.html',context)

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
        'AboutSlider' : AboutSlider,
        'AboutFeedback' : AboutFeedback,
        'AboutService' : AboutService,
        'AboutExperience' : AboutExperience,
        'AboutUs' : AboutUs,
        'AboutUsItem' : AboutUsItem,
        'Gallery' : Gallery,
        'Chef' : Chef,
        'ChefItem' : ChefItem,
        'FeedbackItem' : FeedbackItem,
        }
    return render(request,'about.html',context)
