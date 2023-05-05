from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>', views.details, name='product_details'),
    path('search/', views.search, name='search'),
    ]