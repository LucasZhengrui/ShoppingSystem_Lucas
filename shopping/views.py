from django.core.paginator import Paginator
from django.shortcuts import render
from .models import basicinfo, detail

# Create your views here.
def product_list(request):
    products = basicinfo.info()
    paginator = Paginator(products, 10) # show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopping/product_list.html', {'page_obj': page_obj})

def product__by_id(request, Unique_id):
    products = detail.shopping_by_id(Unique_id)
    paginator = Paginator(products, 1) # show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopping/product_detail.html', {'page_obj': page_obj})