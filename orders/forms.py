from django import forms

from orders.models import Order


class OrdersForm(forms.ModelForm):
    first_name = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ivanov@example.ru'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Россия, Москва, ул.Мира, д 2'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')