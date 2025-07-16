from django.urls import path
from . import views

urlpatterns=[
    path('sea',views.sea_views,name="sea_views")
]
