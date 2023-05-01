from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import detail, basicinfo, Message
from shopping.views import get_message_obj, product_list
from django.http import HttpResponseRedirect
import sqlite3

# Create your views here.
# Order part

# Order stuff part

def get_product():
    order = detail.objects.order_by('Unique_id').filter(Is_deleted=0)
    return order

def index(request):
    order = get_product()

    # Search
    search_query = request.GET.get('search_query')
    search_field = request.GET.get('search_field', 'all')
    if search_query and search_field != 'all':
        order = order.filter(**{search_field: search_query})

    # Pagination
    paginator = Paginator(order, 10)  # Show 10 items per page
    page = request.GET.get('page', 1)

    try:
        # Convert page to an integer
        page = int(page)
        # Validate that the page is greater than or equal to 1
        if page <= 0:
            page = 1
        # Get the page from the paginator
        orders = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        # If page is not an integer or out of range, deliver first page.
        orders = paginator.page(1)

    # Limit the page range to 3 pages
    page_range = paginator.get_elided_page_range(page, on_each_side=0, on_ends=1)

    message_obj = get_message_obj()

    return render(request, 'order/product_detail.html', {'order': orders, 'search_query': search_query,
                                                         'search_field': search_field, 'page_range': page_range, 'message_obj':message_obj})

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