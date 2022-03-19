from django import forms
from .models import Product


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
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'id': 'item-name', 'type': 'text'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'id': 'about-textarea'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'type': 'number'})
        self.fields['count'].widget.attrs.update({'class': 'form-control', 'id': 'count-textarea', 'type': 'number'})
