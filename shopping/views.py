from django.core.paginator import Paginator
from django.shortcuts import render
from .models import basicinfo, detail, Message
import sqlite3

# Create your views here.

def get_message_obj():
    message_obj = Message.objects.order_by('-id')
    return message_obj

def index(request, id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM shopping_basicinfo AS a LEFT JOIN shopping_detail AS b ON a.id = b.id WHERE a.id = ?', (id,))
    myList = cursor.fetchall()
    message_obj = get_message_obj()
    connection.close()
    return render(request, 'shopping/product_detail.html', {'list': myList, 'message_obj': message_obj})

def product_list(request):
    products = basicinfo.info()
    paginator = Paginator(products, 10) # show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopping/product_list.html', {'page_obj': page_obj})

# def product__by_id(request, Unique_id):
#     products = detail.shopping_by_id(Unique_id)
#     paginator = Paginator(products, 1) # show 10 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'shopping/product_detail.html', {'page_obj': page_obj})