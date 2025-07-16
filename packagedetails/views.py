from django.shortcuts import render

# Create your views here.

def packdetails_views(request):
    return render(request,"packagedetails.html")