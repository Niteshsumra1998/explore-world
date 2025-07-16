from django.urls import path
from . import views

urlpatterns=[
    path('',views.packdetails_views,name="packdetails_views")
]