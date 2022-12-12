from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = "food"

urlpatterns = [
    path('', login_required(views.indexClassView.as_view()), name = "index"), 
    path("<int:pk>/", views.detailClassView.as_view(), name = "detail"),
    path("add/", views.add_item, name = "add_item"),
    path('delete/<int:id>/', views.delete_item, name = "delete_item"),
]