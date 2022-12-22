
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import RegisterUserForm, LoginUserForm, AddProductForm, AddOrderForm, AddCustomerForm
from .models import Product, Order, Customer
from .utils import DataMixin
from .filters import OrderFilter


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
    context = {'name': request.user_name,
                        'title' : 'About'}
    return render(request, 'crm/about.html', context)



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



class ShowProducts(DataMixin, ListView):
    model = Product
    template_name = 'crm/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'])
        return dict(list(context.items()) + list(c_def.items()))

    # def get_queryset(self):
    #     return Order.objects.all().order_by('date_created')



class ProductDetail(DataMixin, DetailView):
    model = Product
    template_name = 'crm/product_detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))



class AddOrder(DataMixin,CreateView):
    model = Order
    form_class = AddOrderForm
    template_name = 'crm/add_order.html' 
    login_url = reverse_lazy('login')
    success_url = 'home'
    


    def get_initial(self):
        initial = super(AddOrder, self).get_initial()
        customer_id = self.kwargs['customer']
        initial['customer'] = Customer.objects.get(pk=customer_id)
        return initial




class ShowOrders(DataMixin, ListView):
    model = Order
    template_name = 'crm/orders_list.html'
    
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['orders'])
        return dict(list(context.items()) + list(c_def.items()))
    



class OrderDetail(DataMixin, DetailView):
    model = Order
    template_name = 'crm/oreder_detail.html'
    pk_url_kwarg = 'order_id'
    context_object_name = 'order'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['order'])
        return dict(list(context.items()) + list(c_def.items()))



class AddCustomer(DataMixin, CreateView):
    template_name = 'crm/add_customer.html'
    form_class = AddCustomerForm
    success_url = reverse_lazy('customers-list')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Create customer')
        return dict(list(context.items()) + list(c_def.items()))



class ShowCustomers(DataMixin, ListView):
    template_name = 'crm/customers_list.html'
    model = Customer
    context_object_name = 'customers'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='customers')
        return dict(list(context.items()) + list(c_def.items()))

 


class CustomerDetail(DataMixin, DetailView):
    model = Customer
    template_name = 'crm/customer_detail.html'
    pk_url_kwarg = 'customer_id'
    context_object_name = 'customer'
    
    def get(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        total_orders = orders.count()
        # Search Functionality
        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs
        total_orders = orders.count()
        context = {'customer': customer, 'orders': orders,
                'total_orders': total_orders, 'myFilter': myFilter}

        return render(request, 'crm/customer_detail.html', context)


