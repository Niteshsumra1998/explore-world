from django.urls import path
from . import views

urlpatterns=[
    path('',views.blogs_view,name="blogs_view")
]