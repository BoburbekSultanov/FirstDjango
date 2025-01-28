from django.contrib import admin

from apps.models import Jobs, Category, Product, Tariff, Image


# Register your models here.

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass