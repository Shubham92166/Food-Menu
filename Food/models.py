from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class item(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 200, default = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJrurcz8RuuhpJ3MAUaFGANA-8CClm7YPKfSiC6Sgzhs81NM2sS4da40mAX74yet8rIQk&usqp=CAU")
    