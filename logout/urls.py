from django.urls import path
from . import views

urlpatterns=[
    path('',views.logout_views,name="logout_views")
]