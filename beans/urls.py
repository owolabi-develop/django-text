from django.urls import path, include
from . import views

urlpatterns = [
    path("Index/",views.index,name="Index")
    
]
