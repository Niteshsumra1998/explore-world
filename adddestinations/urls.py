from django.urls import path
from . import views

urlpatterns=[
    path('',views.add_destination,name="add_destination")
]