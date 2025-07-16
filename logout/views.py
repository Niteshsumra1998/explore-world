from django.shortcuts import render,redirect

# Create your views here.

def logout_views(request):
    request.session["username"]=""
    request.session["userole"]=""
    return redirect("home")