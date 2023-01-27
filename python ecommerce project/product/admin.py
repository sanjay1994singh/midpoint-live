from django.contrib import admin
from .models import ProductMaster, BrandMaster,CategoryMaster
# Register your models here.
admin.site.register(BrandMaster)
admin.site.register(CategoryMaster)
admin.site.register(ProductMaster)
