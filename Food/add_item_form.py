from cProfile import label
from tkinter import Widget
from typing import ItemsView
from django import forms
from .models import item

class addItem(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        

