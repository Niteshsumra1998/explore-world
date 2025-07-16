from django.urls import path
from . import views

urlpatterns=[
    path('',views.additernay_views,name="additernay_views")
]