from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hi, you're at the django_knit index.")


def detail(request, product_id):
    return HttpResponse("it's detail of %s." % product_id)


def edit(request, product_id):
    return HttpResponse("it's editing of %s." % product_id)
