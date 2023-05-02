from django.db import models
from shopping.models import Message
from django.urls import reverse

# Create your models here.
class clients(models.Model): # Here is the creating period for user info's database
    User_id = models.IntegerField(primary_key=True)
    User_psd = models.TextField()
    User_nickname = models.TextField()
    User_status = models.TextField()

    class Meta:
        db_table = 'Clients_table'
    
    def __str__(self):
        return "User ID: {self.User_id}, User Nicename: {self.User_name}"
    
    def get_absolute_url(self):
        return reverse('user.info', kwargs={'pk': self.pk})