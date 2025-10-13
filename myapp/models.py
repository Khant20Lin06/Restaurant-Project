from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
# Create your models here.


##################### Home Page ###########################
# MainSlider
class MainSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    into1 = models.CharField(max_length=50, blank=True, null=True)
    into2 = models.CharField(max_length=50, blank=True, null=True)
    into3 = models.CharField(max_length=50, blank=True, null=True)
    into4 = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    menu = models.CharField(max_length=50, blank=True, null=True)
    num = models.CharField(max_length=50, blank=True, null=True)
    bgImage = models.ImageField(upload_to='MainSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# BestMenu


class BestMenuModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Unnamed Category"

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Unnamed Tag"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)           # Normal price
    disPrice = models.IntegerField(blank=True, null=True)        # Discounted price
    discountPercentage = models.IntegerField(blank=True, null=True, editable=False)  # Auto calculated
    image = models.ImageField(upload_to="Product")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discountPercentage(self):
        if self.price and self.disPrice and self.price > 0:
            return round(((self.price - self.disPrice) / self.price) * 100)
        return 0
    
    def __str__(self):
        return self.title or "Untitled Product"


class ProductDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)           # Normal price
    disPrice = models.IntegerField( blank=True, null=True)        # Discounted price
    discountPercentage = models.IntegerField(blank=True, null=True, editable=False)  # Auto calculated
    SKU = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discountPercentage(self):
        if self.price and self.disPrice and self.price > 0:
            return round(((self.price - self.disPrice) / self.price) * 100)
        return 0

    def __str__(self):
        return self.title or "Untitled Product Detail"

class ProductImageModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        ProductDetail, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="ProductImage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MenuModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tImage = models.ImageField(upload_to='Menu')
    bImage = models.ImageField(upload_to='Menu')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# About


class AboutModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    into = models.CharField(max_length=200, blank=True, null=True)
    pName = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='About')
    topImage = models.ImageField(upload_to='About')
    sideImage1 = models.ImageField(upload_to='About')
    sideImage2 = models.ImageField(upload_to='About')
    clientImage = models.ImageField(upload_to='About')
    pImage = models.ImageField(upload_to='About')
    thm_text = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Promotion


class PromotionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    discount = models.CharField(max_length=50, blank=True, null=True)
    promotion = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='Promotion')
    day = models.CharField(max_length=50, blank=True, null=True)
    hour = models.CharField(max_length=50, blank=True, null=True)
    min = models.CharField(max_length=50, blank=True, null=True)
    sec = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Strength


class StrengthModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StrengthItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    description1 = models.CharField(max_length=300, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
    description2 = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Rate


class RateModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=500, blank=True, null=True)
    rate0 = models.CharField(max_length=50, blank=True, null=True)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    rate1 = models.CharField(max_length=500, blank=True, null=True)
    rate11 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
    rate2 = models.CharField(max_length=500, blank=True, null=True)
    rate22 = models.CharField(max_length=50, blank=True, null=True)
    name3 = models.CharField(max_length=50, blank=True, null=True)
    rate3 = models.CharField(max_length=500, blank=True, null=True)
    rate33 = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# DownloadAPP


class DownloadAPPModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='DownloadAPP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Chef


class ChefModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tImage = models.ImageField(upload_to='Chef')
    bImage = models.ImageField(upload_to='Chef')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChefItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='ChefItem')
    fb = models.CharField(max_length=300, blank=True, null=True)
    x = models.CharField(max_length=300, blank=True, null=True)
    ig = models.CharField(max_length=300, blank=True, null=True)
    linkIn = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# BookTable


class BookTableModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    title1 = models.CharField(max_length=50, blank=True, null=True)
    tag1 = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    lImage = models.ImageField(upload_to='BookTable')
    bImage = models.ImageField(upload_to='BookTable')
    thm_text = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DateTimeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookTableOrderListModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    guest = models.CharField(max_length=50, blank=True, null=True)
    massage = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Feedback


class FeedbackModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    tImage = models.ImageField(upload_to='Feedback')
    bImage = models.ImageField(upload_to='Feedback')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeedbackItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=500, blank=True, null=True)
    profileImage = models.ImageField(upload_to='FeedbackItem')
    image = models.ImageField(upload_to='FeedbackItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Blog


class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    lImage = models.ImageField(upload_to='Blog')
    rImage = models.ImageField(upload_to='Blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BlogItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    food = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='BlogItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### Menu Page #######################

class MenuSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='MenuSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MenuCategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category1 = models.CharField(max_length=50, blank=True, null=True)
    category11 = models.CharField(max_length=50, blank=True, null=True)
    image1 = models.ImageField(upload_to='MenuCategory')
    category2 = models.CharField(max_length=50, blank=True, null=True)
    category22 = models.CharField(max_length=50, blank=True, null=True)
    image2 = models.ImageField(upload_to='MenuCategory')
    category3 = models.CharField(max_length=50, blank=True, null=True)
    category33 = models.CharField(max_length=50, blank=True, null=True)
    image3 = models.ImageField(upload_to='MenuCategory')
    category4 = models.CharField(max_length=50, blank=True, null=True)
    category44 = models.CharField(max_length=50, blank=True, null=True)
    image4 = models.ImageField(upload_to='MenuCategory')
    category5 = models.CharField(max_length=50, blank=True, null=True)
    category55 = models.CharField(max_length=50, blank=True, null=True)
    image5 = models.ImageField(upload_to='MenuCategory')
    category6 = models.CharField(max_length=50, blank=True, null=True)
    category66 = models.CharField(max_length=50, blank=True, null=True)
    image6 = models.ImageField(upload_to='MenuCategory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GalleryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='Gallery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### Shop Page #######################

class ShopSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='ShopSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### Shop Detail Page #######################

class ShopDetailSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='ShopDetailSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DescriptionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### New Page #######################

class NewSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='NewSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TagModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfileModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    fb = models.CharField(max_length=50, blank=True, null=True)
    x = models.CharField(max_length=50, blank=True, null=True)
    p = models.CharField(max_length=50, blank=True, null=True)
    linkIn = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='Profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='Post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    food = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='New')
    name1 = models.CharField(max_length=50, blank=True, null=True)
    date1 = models.CharField(max_length=50, blank=True, null=True)
    comment1 = models.CharField(max_length=50, blank=True, null=True)
    food1 = models.CharField(max_length=50, blank=True, null=True)
    title1 = models.CharField(max_length=50, blank=True, null=True)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='New')
    image2 = models.ImageField(upload_to='New')
    name2 = models.CharField(max_length=50, blank=True, null=True)
    date2 = models.CharField(max_length=50, blank=True, null=True)
    comment2 = models.CharField(max_length=50, blank=True, null=True)
    food2 = models.CharField(max_length=50, blank=True, null=True)
    title2 = models.CharField(max_length=50, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
    name3 = models.CharField(max_length=50, blank=True, null=True)
    date3 = models.CharField(max_length=50, blank=True, null=True)
    comment3 = models.CharField(max_length=50, blank=True, null=True)
    food3 = models.CharField(max_length=50, blank=True, null=True)
    title3 = models.CharField(max_length=50, blank=True, null=True)
    description3 = models.CharField(max_length=500, blank=True, null=True)
    video3 = models.CharField(max_length=50, blank=True, null=True)
    image3 = models.ImageField(upload_to='New')
    name4 = models.CharField(max_length=50, blank=True, null=True)
    name44 = models.CharField(max_length=50, blank=True, null=True)
    date4 = models.CharField(max_length=50, blank=True, null=True)
    comment4 = models.CharField(max_length=50, blank=True, null=True)
    food4 = models.CharField(max_length=50, blank=True, null=True)
    title4 = models.CharField(max_length=50, blank=True, null=True)
    description4 = models.CharField(max_length=500, blank=True, null=True)
    video4 = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### New Detail Page #######################

class NewDetailSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='NewDetailSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='NewDetail')
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    food = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=500, blank=True, null=True)
    text2 = models.CharField(max_length=500, blank=True, null=True)
    text3 = models.CharField(max_length=500, blank=True, null=True)
    text4 = models.CharField(max_length=500, blank=True, null=True)
    tag = models.CharField(max_length=500, blank=True, null=True)
    text5 = models.CharField(max_length=500, blank=True, null=True)
    text6 = models.CharField(max_length=500, blank=True, null=True)
    title1 = models.CharField(max_length=50, blank=True, null=True)
    text7 = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    text8 = models.CharField(max_length=500, blank=True, null=True)
    text9 = models.CharField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='NewDetail')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewDetailTagModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    fb = models.CharField(max_length=500, blank=True, null=True)
    x = models.CharField(max_length=500, blank=True, null=True)
    linkIn = models.CharField(max_length=500, blank=True, null=True)
    ig = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### Contact Page #######################

class ContactSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='Contact')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title1 = models.CharField(max_length=50, blank=True, null=True)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    name11 = models.CharField(max_length=50, blank=True, null=True)
    title2 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
    name22 = models.CharField(max_length=50, blank=True, null=True)
    title3 = models.CharField(max_length=50, blank=True, null=True)
    name3 = models.CharField(max_length=50, blank=True, null=True)
    name33 = models.CharField(max_length=50, blank=True, null=True)
    title4 = models.CharField(max_length=50, blank=True, null=True)
    name4 = models.CharField(max_length=50, blank=True, null=True)
    name44 = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### About Page #######################

class AboutSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='AboutSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutFeedbackModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='AboutFeedback')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutExperienceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='AboutExperience')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    description1 = models.CharField(max_length=400, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
    description2 = models.CharField(max_length=400, blank=True, null=True)
    name3 = models.CharField(max_length=50, blank=True, null=True)
    description3 = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutUsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to='AboutUs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutUsItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### Cart Page #######################

class CartSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='CartSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### WishList Page #######################

class WishListSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='WishListSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#################### CheckOut Page #######################

class CheckOutSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='CheckOutSlider')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class CustomUser(AbstractUser):
    # custom fields
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('guest', 'Guest'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # conflict မဖြစ်အောင် related_name ပြောင်း
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # conflict မဖြစ်အောင် related_name ပြောင်း
        blank=True
    )