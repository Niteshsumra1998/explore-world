from django.shortcuts import render
from adddestinations.adddestimodel import destinationCatalogClass
from django.contrib import messages
# Create your views here.

def addpackiternary_views(request):
    if request.method=="POST":
        # vpname=request.POST.get("dname")
        vdesid=request.POST.get("destination_id")
        vtravel=request.POST.get("travel")
        vstay=request.POST.get("stay")
        vprice=request.POST.get("pprice")
        result=destinationCatalogClass.adddestinationpackages(vdesid,vtravel,vstay,vprice)
        messages.success(request,result)
    vdestidname=destinationCatalogClass.getalldestname()
    context={
        'destidnm':vdestidname,
    }
    return render(request,"addpackiternary.html",context)