from django.urls import path
from . import views

urlpatterns=[
    path('',views.addpackiternary_views,name="addpackiternary_views")
]