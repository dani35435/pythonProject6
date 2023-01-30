from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about', About.as_view(), name='about'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('products', Products.as_view(), name='products'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('login', Login.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)