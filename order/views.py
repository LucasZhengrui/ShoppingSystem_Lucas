from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import detail, basicinfo, Message
from shopping.views import get_message_obj, product_list
from django.http import HttpResponseRedirect
import sqlite3

# Create your views here.
# Order part

# Order stuff part

def order(request, id):
    order = detail.objects.get(id=id) # The 'id' in this place should be the unique one which was created by shopping/model (build database or read csv)
    order.Is_deleted = 1
    order.save()
    return product_list(request)

# Cancel order part

def get_order():
    order = detail.objects.order_by('Unique_id').filter(Is_deleted=1)
    return order

def order_list(request):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM shopping_basicinfo AS a LEFT JOIN shopping_detail AS b ON a.id = b.id WHERE b.Is_deleted = 1')
    myList = cursor.fetchall()
    message_obj = get_message_obj()
    connection.close()
    return render(request, 'order/order_list.html', {'list': myList, 'message_obj': message_obj})

def cancel(request, id):
    product = detail.objects.get(id=id) # The 'id' in this place should be the unique one which was created by shopping/model (build database or read csv)
    product.Is_deleted = 0
    product.save()
    return HttpResponseRedirect('/cart')