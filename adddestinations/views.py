from django.shortcuts import render
from adddestinations.adddestimodel import destinationCatalogClass
from django.contrib import messages
# Create your views here.

def add_destination(request):
    vusername=request.session.get("username")

    context={
        'candidatename':vusername
    }
    
    if request.method=="POST":
        vpname=request.POST.get("dname")
        vpdesc=request.POST.get("ddesc")
        vpprice=request.POST.get("dprice")
        vpimage=request.POST.get("dimage")
        msg=destinationCatalogClass.adddestionationRecord(vpname,vpdesc,vpprice,vpimage)
        print(msg)
        splitmsg=msg.split(":")
        print(splitmsg[0])
        
        if splitmsg[0]=="Error":
            messages.error(request,splitmsg[1])
        else:
            messages.success(request,splitmsg[1])
    
    return render(request,"destinationcatalog.html",context)