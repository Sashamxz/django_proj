
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import RegisterUserForm, LoginUserForm, AddProductForm, CustomerForm
from .models import Product, Order, Customer
from .utils import DataMixin



#auth views
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'crm/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')




class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'crm/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Loging")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



def logout_user(request):
    logout(request)
    return redirect('login')






#common views
class CrmHome(DataMixin, ListView):
    model = Customer
    template_name = 'crm/index.html'
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        context['customers'] = Customer.objects.all()
        c_def = self.get_user_context(title="Home page")
        return dict(list(context.items()) + list(c_def.items()))
   




def about(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'crm/about.html', {'page_obj': page_obj,  'title': 'About'})





#crm views
class AddProduct(DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'crm/add_product.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True
 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add product')
        return dict(list(context.items()) + list(c_def.items()))





class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'crm/product.html'
    
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))





class ShowOrders(DataMixin, DetailView):
    model = Order
    template_name = 'crm/orders.html'
    
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


class CreateCustomer(DataMixin, CreateView):
    template_name = 'crm/customer_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Create customer')
        return dict(list(context.items()) + list(c_def.items()))


def customer_list(request):
    customers = Customer.objects.all()
    context =  {'customers': customers,}
    return render(request, 'crm/list_customers.html', context)





class CustomerDetail(DataMixin, DetailView):
    model = Customer
    template_name = 'crm/customer.html'
    pk_url_kwarg = 'customer_pk'
    context_object_name = 'customer'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['customer'])
        return dict(list(context.items()) + list(c_def.items()))





class CreateOrder(DataMixin,CreateView):
    model = Order
    template_name = 'crm/add_order.html' 
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Create order')
        return dict(list(context.items()) + list(c_def.items()))