from django.urls import path
from . import views

urlpatterns=[
    path('',views.moredetails_view,name="moredetails_view")
]