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

# def index(request):
#     return render(request, 'usersgroup/index.html')

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
        
        Password_md5_signup = hashlib.md5(User_psd.encode('utf-8')).hexdigest()
        User_name = request.POST.get('name')
        Status = 0

        # create a new user in the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clients_table (User_psd, User_nickname, User_status) VALUES (?, ?, ?)", (Password_md5_signup, User_name, Status))
        conn.commit()
        conn.close()

        response = goto_index_view(request,'/')
        return response
    else:
        return render(request, 'usersgroup/register.html')
    
def login(request):
    if request.method == 'POST':
        # Get the user nickname and password
        Nickname = request.POST.get('Nickname')
        Password = request.POST.get('Password')

        # Search user in the database
        try:
            user = clients.objects.get(User_nickname=Nickname)
        except clients.DoesNotExist:
            error_message = 'Bad luck, user is not found!'
            return render(request, 'usersgroup/login.html', {'error_message': error_message})

        # Check password, is it correct?
        Password_md5 = hashlib.md5(Password.encode('utf-8')).hexdigest()
        if Password_md5 != user.User_psd:
            error_message = 'Password is incorrect!'
            return render(request, 'usersgroup/login.html', {'error_message': error_message})

        # Set user login status to "logged in"
        user.User_status = 1 # 0 means the user doesn't login, 1 means the user has logged in to their account
        user.save()

        # Create a response object and set a cookie
        response = goto_index_view(request,'/')
        response.set_cookie('Nickname', Nickname)

        return response

    else:
        response = render(request, 'usersgroup/login.html')
        Nickname = request.COOKIES.get('Nickname')
        try:
            user = clients.objects.get(User_nickname=Nickname)
            user.User_status = 0
            user.save()
        except clients.DoesNotExist:
            pass
        
        response.delete_cookie('Nickname')
        return response
