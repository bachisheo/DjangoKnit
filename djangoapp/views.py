from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product

# Create your views here.

class IndexView(ListView):
    model = Product
    template_name = 'djangoapp/index.html'

def detail(request, product_id):
    return HttpResponse("it's detail of %s." % product_id)


def edit(request, product_id):
    return HttpResponse("it's editing of %s." % product_id)
