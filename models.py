# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClientsTable(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    user_nickname = models.TextField(db_column='User_nickname', blank=True, null=True)  # Field name made lowercase.
    user_status = models.TextField(db_column='User_status')  # Field name made lowercase.
    password = models.TextField()
    user_email = models.CharField(db_column='User_email', unique=True, max_length=254)  # Field name made lowercase.
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clients_table'


class ClientsTableGroups(models.Model):
    clients = models.ForeignKey(ClientsTable, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Clients_table_groups'
        unique_together = (('clients', 'group'),)


class ClientsTableUserPermissions(models.Model):
    clients = models.ForeignKey(ClientsTable, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Clients_table_user_permissions'
        unique_together = (('clients', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DisasterMessage(models.Model):
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'disaster_message'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ShoppingBasicinfo(models.Model):
    unique_id = models.TextField(db_column='Unique_id')  # Field name made lowercase.
    product_name = models.TextField(db_column='Product_name')  # Field name made lowercase.
    brand_name = models.TextField(db_column='Brand_name')  # Field name made lowercase.
    selling_price = models.TextField(db_column='Selling_price')  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    amazon_seller = models.TextField(db_column='Amazon_seller')  # Field name made lowercase.
    category = models.TextField(db_column='Category')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shopping_basicinfo'


class ShoppingDetail(models.Model):
    model_number = models.TextField(db_column='Model_number')  # Field name made lowercase.
    about_product = models.TextField(db_column='About_product')  # Field name made lowercase.
    product_specification = models.TextField(db_column='Product_specification')  # Field name made lowercase.
    shipping_weight = models.TextField(db_column='Shipping_weight')  # Field name made lowercase.
    product_dimensions = models.TextField(db_column='Product_dimensions')  # Field name made lowercase.
    unique_id = models.ForeignKey(ShoppingBasicinfo, models.DO_NOTHING, db_column='Unique_id_id')  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='Is_deleted')  # Field name made lowercase.
    technical_details = models.TextField(db_column='Technical_details')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shopping_detail'
