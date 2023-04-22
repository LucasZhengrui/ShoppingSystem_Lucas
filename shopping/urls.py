from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:Unique_id>', views.product__by_id, name='product_details'),
    ]