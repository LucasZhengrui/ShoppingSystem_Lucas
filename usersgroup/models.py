from django.db import models
from shopping.models import Message

# Create your models here.
class clients(models.Model):
    User_id = models.IntegerField(primary_key=True)
    User_psd = models.TextField()
    User_nickname = models.TextField()
    User_status = models.TextField()

    class Meta:
        db_table = 'Clients_table'
    
    def __str__(self):
        return "User ID: {self.User_id}, User Nicename: {self.User_name}"