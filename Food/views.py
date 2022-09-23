from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import item
from django.template import loader
# Create your views here.
def index(request):
    allItems = item.objects.all()
    
    context = {
        'allItems' : allItems
     }
    return render(request, "Food/index.html", context)

def detail(request, item_id):
    item_detail = item.objects.get(pk = item_id)
    context = {
        'item_detail' : item_detail,
    }
    return render(request, "Food/detail.html", context)

   