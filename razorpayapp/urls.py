from django.urls import path
from . import views

urlpatterns=[
    path('',views.razorpay_views,name="razorpay_views"),
    path('paymenthandler/',views.paymenthandler,name="paymenthandler")
]