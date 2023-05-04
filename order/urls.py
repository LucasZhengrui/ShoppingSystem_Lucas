from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.order_list, name='cart'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('addcart/<int:id>', views.order, name='addcart'),
    ]