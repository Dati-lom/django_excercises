from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

#/home
def index(request):
    return HttpResponse("<h1>Main Page</h1>", status=200)
#/item
def item_page(request):
    return HttpResponse("<h1>This is Item Page</h1>", status=200)