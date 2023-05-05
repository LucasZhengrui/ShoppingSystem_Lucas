from django.test import Client, TestCase
from .models import clients
import hashlib

# Create your tests here.

class UserTestCase(TestCase):
    def setup(self):
      clients.objects.create(User_Nickname="Testuser", password=hashlib.md5("testpassword".encode('utf-8')).hexdigest())

def test_login(self):
    client = Client()
    response = client.post('/login/', {'User_Nickname': 'testuser', 'password': 'testpassword'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/')
    self.assertEqual(client.cookies.get('User_Nickname').value, 'Testuser')

def test_wrong_login(self):
    client = Client()
    response = client.post('/login/', {'User_Nickname': 'testuser', 'password': 'Ahatestpassword'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'usersgroup/login.html')
    self.assertContains(response, 'Password is incorrect!')

def test_register(self):
    client = Client()
    response = client.post('/register/', {'User_Nickname': 'testuser', 'password': 'testpassword'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, '/')
    user = clients.objects.get(User_Nickname='testuser')
    self.assertEqual(user.User_Nickname, 'testuser')