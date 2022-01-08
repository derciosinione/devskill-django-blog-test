from django.urls import path
from . import views

urlpatterns = [
    # Your code here
    path('', views.index, name='index'),
]
