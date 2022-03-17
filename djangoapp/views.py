from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product


# Create your views here.

class IndexView(ListView):
    model = Product
    template_name = 'djangoapp/index.html'


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'djangoapp/detail.html', {'product': product})



def edit(request, product_id):
    return HttpResponse("it's editing of %s." % product_id)
