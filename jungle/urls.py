from django.urls import path
from . import views

urlpatterns=[
    path('',views.wildlife_views,name="wildlife_views")
]