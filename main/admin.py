from django.contrib import admin
from .models import Product, Category, Post, Banner, Visitor, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)
    #list_filter = ('category', 'product_category')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Visitor) 