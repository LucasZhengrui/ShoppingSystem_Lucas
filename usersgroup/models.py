from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.urls import reverse_lazy

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class clients(AbstractBaseUser, PermissionsMixin):
    User_id = models.IntegerField(primary_key=True)
    password = models.TextField()
    User_nickname = models.TextField(null=True, default='Guest')
    User_status = models.TextField()
    User_email = models.EmailField(default='abcd@mail.com', unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='user_clients')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_clients')

    # The following two lines to use your custom UserManager
    objects = MyUserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'Clients_table'
    
    def __str__(self):
        return f"User ID: {self.User_id}, User Nicename: {self.User_nickname}"
    
    def get_absolute_url(self):
        return reverse_lazy('user.info', kwargs={'pk': self.pk})