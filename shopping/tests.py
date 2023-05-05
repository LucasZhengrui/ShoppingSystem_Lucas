from django.test import TestCase, Client
from .models import basicinfo

# Create your tests here.
class Product_test(TestCase):
    def setup(self):
        basicinfo.objects.create(Unique_id='8001', Product_name='UNO', Brand_name='UNO',
                                    Category='Toys', Selling_price='10 pounds',
                                    Image='https://i.imgur.com/pwuBwJH.png', Amazon_seller='Y')
        basicinfo.objects.create(Unique_id='8002', Product_name='UNO1', Brand_name='UNO1',
                                    Category='Toys1', Selling_price='20 pounds',
                                    Image='https://i.imgur.com/pwuBwJH.png', Amazon_seller='Y')

    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/product_list.html')
        self.assertContains(response, 'UNO')
        self.assertContains(response, 'UNO1')

    def test_search(self):
        client = Client()
        response = client.get('/search/?search_field=Category&search_query=Toys')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping/product_list.html')
        self.assertContains(response, 'UNO')
        self.assertContains(response, 'UNO1')