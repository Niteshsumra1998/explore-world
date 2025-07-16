from django.urls import path
from . import views

urlpatterns=[
    path('mountains',views.mount_views,name="mount_views")
]