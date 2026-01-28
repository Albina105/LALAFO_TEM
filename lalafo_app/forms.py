from . models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_price','phone_number','description','product_type','image']
        widgets = {
            'product_name': forms.TextInput(attrs={
                'placeholder': 'Введите название продукта',
                'class': 'input-field'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Введите описание',
                'class': 'input-field'
            }),
            'product_price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'input-field'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Введите номер телефона',
                'class': 'input-field'
            }),
            'product_type': forms.TextInput(attrs={
                'placeholder': 'Введите тип продукта ',
                'class': 'input-field'
            }),
        }