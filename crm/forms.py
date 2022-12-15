from django.forms import ModelForm
from .models import Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Customer, Product



#name.price.categore.description

class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.IntegerField(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('More than 30 letter')

        return name





class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'email']
		exclude = ['user']



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']


