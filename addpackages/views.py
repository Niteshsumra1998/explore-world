from django.shortcuts import render
from addpackages.addpackagemodel import packageCatalogClass
from django.contrib import messages
# Create your views here.

def packages_view(request):
    vusername=request.session.get("username")

    context={
        'candidatename':vusername
    }
    
    if request.method=="POST":
        pname=request.POST.get("pname")
        pdesc=request.POST.get("pdesc")
        pprice=request.POST.get("pprice")
        pimage=request.POST.get("pimage")
        msg=packageCatalogClass.addpackageRecord(pname,pdesc,pprice,pimage)
        print(msg)
        splitmsg=msg.split(":")
        print(splitmsg[0])
        
        if splitmsg[0]=="Error":
            messages.error(request,splitmsg[1])
        else:
            messages.success(request,splitmsg[1])
    
    return render(request,"packagescatalog.html",context)