from django.contrib import admin
from .models import *
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

##### HomePage ############

admin.site.register(MainSliderModel)
admin.site.register(BestMenuModel)
admin.site.register(MenuModel)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductDetail, ProductAdmin)
admin.site.register(AboutModel)
admin.site.register(AboutItemModel)
admin.site.register(PromotionModel)
admin.site.register(StrengthModel)
admin.site.register(StrengthItemModel)
admin.site.register(RateModel)
admin.site.register(DownloadAPPModel)
admin.site.register(ChefModel)
admin.site.register(ChefItemModel)
admin.site.register(BookTableModel)
admin.site.register(DateTimeModel)
admin.site.register(BookTableOrderListModel)
admin.site.register(FeedbackModel)
admin.site.register(FeedbackItemModel)
admin.site.register(BlogModel)
admin.site.register(BlogItemModel)
admin.site.register(CategoryModel)


######## MenuPage ##########

admin.site.register(MenuSliderModel)
admin.site.register(MenuCategoryModel)
admin.site.register(GalleryModel)


######## ShopPage ##########

admin.site.register(ShopSliderModel)



######## ShopDetailPage ##########

admin.site.register(ShopDetailSliderModel)
admin.site.register(DescriptionModel)
admin.site.register(ProductModel)



######## NewPage ##########

admin.site.register(NewSliderModel)
admin.site.register(TagModel)
admin.site.register(ProfileModel)
admin.site.register(PostModel)
admin.site.register(NewModel)




######## NewDetailPage ##########

admin.site.register(NewDetailSliderModel)
admin.site.register(NewDetailTagModel)
admin.site.register(NewDetailModel)
admin.site.register(CommentModel)





######## ContactPage ##########

admin.site.register(ContactSliderModel)
admin.site.register(ContactModel)





######## AboutPage ##########

admin.site.register(AboutSliderModel)
admin.site.register(AboutFeedbackModel)
admin.site.register(AboutExperienceModel)
admin.site.register(AboutServiceModel)
admin.site.register(AboutUsModel)
admin.site.register(AboutUsItemModel)





######## CartPage ##########

admin.site.register(CartSliderModel)





######## WishListPage ##########

admin.site.register(WishListSliderModel)
admin.site.register(Profile)





######## CheckOutPage ##########

admin.site.register(CheckOutSliderModel)


