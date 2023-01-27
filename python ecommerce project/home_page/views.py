from django.shortcuts import render

from product.models import ProductMaster

# Create your views here.

def home_page(request):
    all_products = ProductMaster.objects.raw('select * from product_master')
    context = {
        'product':all_products
    }
    return render(request,'home_page.html', context)