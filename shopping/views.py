from django.core.paginator import Paginator
from django.shortcuts import render
from .models import basicinfo, detail

# Create your views here.
def product_list(request):
    products = basicinfo.info()
    paginator = Paginator(products, 50) # show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopping/product_list.html', {'page_obj': page_obj})

# def product__by_id(request, city):
#     cities = detail.city_by_name(city)
#     paginator = Paginator(cities, 50) # show 10 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'cities/city_list.html', {'page_obj': page_obj})