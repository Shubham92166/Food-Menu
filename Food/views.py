from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .add_item_form import *
from .models import item
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    allItems = item.objects.all()
    context = {
        'allItems' : allItems
     }
    return render(request, "Food/index.html", context)

@login_required
def detail(request, item_id):
    item_detail = item.objects.get(pk = item_id)
    context = {
        'item_detail' : item_detail,
    }
    return render(request, "Food/detail.html", context)

@login_required
def add_item(request):
    form = addItem(request.POST)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, "Food/add_item.html", {'form': form})

@login_required
def delete_item(request, id):
    item = item.objects.get(id = id)

    if request == 'POST':
        item.delete()
        return redirect()
