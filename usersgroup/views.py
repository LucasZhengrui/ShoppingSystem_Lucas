from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import clients
import hashlib
import sqlite3
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from shopping.models import Message
from shopping.views import get_message_obj

# Create your views here.

def index(request):
    return render(request, 'usersgroup/index.html')

def goto_index_view(request,url):
    # Redirect to appropriate page
    return HttpResponseRedirect(url)

def register(request):
    Error_message = ""
    if request.method == 'POST':
        # get data from request.POST
        User_psd = request.POST.get('Password')
        User_confirm_psd = request.POST.get('Confirm_Password')
        
        if User_psd != User_confirm_psd:
              Error_message = "Oooops, something wrong! Please insert same password twice!"
              return render(request, 'usersgroup/register.html',{'Error_message':Error_message})
        
        Password_md5 = hashlib.md5(User_psd.encode('utf-8')).hexdigest()
        User_nickname = request.POST.get('Nickname')
        User_status = 0

        # create a new user in the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "INSERT INTO Clients_table (User_psd, User_nickname, User_status) VALUES (?, ?, ?)"
        cursor.execute(query, (Password_md5, User_nickname, User_status))
        conn.commit()
        conn.close()

        response = goto_index_view(request,'/')
        return response
    else:
        return render(request, 'usersgroup/register.html') # Need to be fixed since there is no html file at the moment