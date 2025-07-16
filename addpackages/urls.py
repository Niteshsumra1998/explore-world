from django.urls import path
from . import views

urlpatterns=[
    path('',views.packages_view,name="packages_view")
]