from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.
def index(request):
    allItems = item.objects.all()
    print(allItems)
    return HttpResponse(allItems)
