from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView, ListView
from .forms import ProductForm
from .models import Product


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Contacts(TemplateView):
    template_name = 'contacts.html'


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'


class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    login_url = '/login'
    success_url = '/products'
    form_class = ProductForm
