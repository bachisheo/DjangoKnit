from django import forms
from .models import Product, Category

categories = Category.objects.all().values_list('name')
# creating a form
class ProductForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Product

        # specify fields to be used
        fields = [
            "name",
            "description",
            "price",
            "count",
            "category"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'item-name', 'type': 'text'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'about-textarea'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'count': forms.TextInput(attrs={'class': 'form-control', 'id': 'count-textarea', 'type': 'number'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-select', 'id': 'category-select'}),

        }

