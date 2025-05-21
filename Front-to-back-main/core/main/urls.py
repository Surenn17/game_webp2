from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('contact/',views.Contact,name='contact'),
    path('shop/',views.Shop,name='shop'),
    path('product-details',views.Product,name='product-details')
]