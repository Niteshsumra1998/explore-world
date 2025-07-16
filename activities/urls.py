from django.urls import path
from . import views

urlpatterns=[
    path('',views.activities_views,name="activities_views")
]