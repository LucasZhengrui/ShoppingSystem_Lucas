from django.test import TestCase, Client
from shopping.models import detail

# Create your tests here.

class OrderlistTest(TestCase):
    def setup(self):
        detail.objects.create(Product_name="UNO", Is_deleted=1)