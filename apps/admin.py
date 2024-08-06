from django.contrib import admin

from apps.models import Product, Category, ProductImage, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
