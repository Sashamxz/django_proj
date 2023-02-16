from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Customer, Product


# name.price.categore.description
class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(max_length=200, label=('Enter name')),
    price = forms.CharField(widget=forms.NumberInput),
    description = forms.CharField(max_length=200, label=('Description'))

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('More than 30 letter')

        return name


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label=('Enter name')),
    phone = forms.CharField(widget=forms.NumberInput),
    email = forms.EmailField(max_length=200, label=('Enter email address')),
    description = forms.CharField(max_length=200, label=('Description'))

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'description', 'profile_pic']


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status', 'urgency']
