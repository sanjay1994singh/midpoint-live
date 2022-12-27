from django.shortcuts import render

# Create your views here.
def epaper_form(request):
    return render(request,'index.html')
