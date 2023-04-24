from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class basicinfo(models.Model):
    Unique_id = models.TextField()
    Product_name = models.TextField()
    Brand_name = models.TextField()
    Category = models.TextField()
    Selling_price = models.TextField()
    Image = models.TextField()
    Amazon_seller = models.TextField()

    def __str__(self):
        return f'{self.Unique_id}, {self.Product_name}, {self.Brand_name}, {self.Category}, {self.Selling_price}, {self.Image}, {self.Amazon_seller}'

    def info():
        products = basicinfo.objects.all()
        return products

    def get_absolute_url(self):
        return reverse('order_list', {'pk': self.pk})
    
class detail(models.Model):
    Unique_id = models.ForeignKey('shopping.basicinfo', on_delete=models.CASCADE, related_name='details')
    Is_deleted = models.IntegerField(default=0)
    Model_number = models.TextField()
    About_product = models.TextField()
    Product_specification = models.TextField()
    Technical_details = models.TextField()
    Shipping_weight = models.TextField()
    Product_dimensions = models.TextField()

    def shopping_by_id(product_id):
        product_list = basicinfo.objects.filter(Unique_id = product_id)
        return product_list

    def __str__(self):
        return f'{self.Unique_id}, {self.Is_deleted}, {self.Model_number}, {self.About_product}, {self.Product_specification}, {self.Technical_details}, {self.Shipping_weight}, {self.Product_dimensions}'

    def get_absolute_url(self):
        return reverse('order_list', {'pk': self.pk})
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    class Meta:
        db_table = 'disaster_message'