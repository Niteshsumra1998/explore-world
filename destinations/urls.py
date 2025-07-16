from django.urls import path
from . import views

urlpatterns=[
    path('',views.destionations,name="destinations"),
]