from django.urls import path 
from .views import views,mainSlider,category,product,productDetail,about,aboutItem,order,promotion,bookTable

urlpatterns = [
    path('', views.AdminDashboard, name="admin_dashboard"),

    # Order
    path('orderList/', order.OrderList, name="OrderList"),
    path('orderDelete/delete/<int:pk>/', order.OrderDelete, name="OrderDelete"),

    # BookATable
    path('bookATableList/', bookTable.BookATableList, name="bookATableList"),
    path('bookATableDelete/delete/<int:pk>/', bookTable.BookATableDelete, name="bookATableDelete"),

    # MainSlider
    path('mainsliderlist/', mainSlider.MainSliderList, name="MainSliderList"),
    path('mainslidercreate/', mainSlider.MainSliderCreate, name="MainSliderCreate"),
    path('mainsliderupdate/update/<uuid:pk>/', mainSlider.MainSliderUpdate, name="MainSliderUpdate"),
    path('mainsliderdetail/detail/<uuid:pk>/', mainSlider.MainSliderDetail, name="MainSliderDetail"),
    path('mainsliderdelete/delete/<uuid:pk>/', mainSlider.MainSliderDelete, name="MainSliderDelete"),

    # Category
    path('categoryList/', category.CategoryList, name="CategoryList"),
    path('categoryCreate/', category.CategoryCreate, name="CategoryCreate"),
    path('categoryUpdate/update/<uuid:pk>/', category.CategoryUpdate, name="CategoryUpdate"),
    path('categoryDetail/detail/<uuid:pk>/', category.CategoryDetail, name="CategoryDetail"),
    path('categoryDelete/delete/<uuid:pk>/', category.CategoryDelete, name="CategoryDelete"),

    # Product
    path('productList/', product.ProductList, name="ProductList"),
    path('productCreate/', product.ProductCreate, name="ProductCreate"),
    path('productUpdate/update/<uuid:pk>/', product.ProductUpdate, name="ProductUpdate"),
    path('productDetail/detail/<uuid:pk>/', product.ProductDetail, name="ProductDetail"),
    path('productDelete/delete/<uuid:pk>/', product.ProductDelete, name="ProductDelete"),

    # ProductDetail
    path('productDetailList/', productDetail.ProductDetailList, name="ProductDetailList"),
    path('productDetailCreate/', productDetail.ProductDetailCreate, name="ProductDetailCreate"),
    path('productDetailUpdate/update/<uuid:pk>/', productDetail.ProductDetailUpdate, name="ProductDetailUpdate"),
    path('productDetailDetail/detail/<uuid:pk>/', productDetail.ProductDetailDetail, name="ProductDetailDetail"),
    path('productDetailDelete/delete/<uuid:pk>/', productDetail.ProductDetailDelete, name="ProductDetailDelete"),

    # About
    path('aboutList/', about.AboutList, name="AboutList"),
    path('aboutCreate/', about.AboutCreate, name="AboutCreate"),
    path('aboutUpdate/update/<uuid:pk>/', about.AboutUpdate, name="AboutUpdate"),
    path('aboutDetail/detail/<uuid:pk>/', about.AboutDetail, name="AboutDetail"),
    path('aboutDelete/delete/<uuid:pk>/', about.AboutDelete, name="AboutDelete"),

    # AboutItem
    path('aboutItemList/', aboutItem.AboutItemList, name="AboutItemList"),
    path('aboutItemCreate/', aboutItem.AboutItemCreate, name="AboutItemCreate"),
    path('aboutItemUpdate/update/<uuid:pk>/', aboutItem.AboutItemUpdate, name="AboutItemUpdate"),
    path('aboutItemDetail/detail/<uuid:pk>/', aboutItem.AboutItemDetail, name="AboutItemDetail"),
    path('aboutItemDelete/delete/<uuid:pk>/', aboutItem.AboutItemDelete, name="AboutItemDelete"),

    # Promotion
    path('promotionList/', promotion.PromotionList, name="PromotionList"),
    path('promotionCreate/', promotion.PromotionCreate, name="PromotionCreate"),
    path('promotionUpdate/update/<uuid:pk>/', promotion.PromotionUpdate, name="PromotionUpdate"),
    path('promotionDetail/detail/<uuid:pk>/', promotion.PromotionDetail, name="PromotionDetail"),
    path('promotionDelete/delete/<uuid:pk>/', promotion.PromotionDelete, name="PromotionDelete"),
]