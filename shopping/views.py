from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import basicinfo as ProductList, detail, Message
from django.http import HttpResponseRedirect
import sqlite3

# Create your views here.

# Basic display

def get_message_obj():
    message_obj = Message.objects.order_by('-id')
    return message_obj

def details(request, id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM shopping_basicinfo AS a LEFT JOIN shopping_detail AS b ON a.id = b.id WHERE a.id = ?', (id,))
    myList = cursor.fetchall()
    message_obj = get_message_obj()
    connection.close()
    return render(request, 'shopping/product_detail.html', {'list': myList, 'message_obj': message_obj})

def product_list(request):
    products = ProductList.info()

    # Search feature
    search_query = request.GET.get('search_query')
    search_field = request.GET.get('search_field', 'all')
    # print(search_field)
    # print(search_query) 
    # # Check if the search feature work correctly

    if search_query and search_field != 'all':
        products = products.filter(**{search_field: search_query})
    
    paginator = Paginator(products, 8) # show 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopping/product_list.html', {'page_obj': page_obj})