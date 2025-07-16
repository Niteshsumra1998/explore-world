from django.urls import path
from . import views

urlpatterns=[
    path('',views.loginpage,name="loginpage"),
    path('signup/', views.signup, name='signup'),
]