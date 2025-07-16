from django.urls import path
from . import views

urlpatterns=[
    path('',views.packages_simple,name="packages_simple"),
]