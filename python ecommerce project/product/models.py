from django.db import models

# Create your models here.
class BrandMaster(models.Model):
    brand_id = models.AutoField(primary_key=True,editable=False)
    brand_name =  models.CharField(max_length=100,null=True)
    brand_description = models.TextField(null=True)
    brand_image = models.ImageField(upload_to='brand images', null=True)

    def __str__(self):
        return self.brand_name


class CategoryMaster(models.Model):
    category_id = models.AutoField(primary_key=True,editable=False)
    category_name =  models.CharField(max_length=100,null=True)
    category_description = models.TextField(null=True)
    category_image = models.ImageField(upload_to='category images', null=True)

    def __str__(self):
        return self.category_name


class ProductMaster(models.Model):
    product_id = models.AutoField(primary_key=True,editable=False)
    product_name = models.CharField(max_length=500,null=True)
    product_description = models.TextField(null=True)
    product_brand = models.ForeignKey(BrandMaster, on_delete=models.CASCADE)
    product_category = models.ForeignKey(CategoryMaster, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=True)
    product_price = models.FloatField(null=True)
    product_rating = models.FloatField(null=True)
    product_like = models.IntegerField(null=True)
    product_views = models.TextField(null=True)
    product_sold = models.BigIntegerField(null=True)
    product_image = models.ImageField(upload_to='product images', null=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product_master'









