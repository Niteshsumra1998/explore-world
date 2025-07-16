from django.shortcuts import render
from adddestinations.adddestimodel import destinationCatalogClass

# Create your views here.


def additernay_views(request):
    if request.method=="POST":
        vqty=int(request.POST.get("quantity"))
        vdesid=request.POST.get("destination_id")
        for i in range(1, vqty + 1):
            feature = request.POST.get(f"feature{i}")
            vresult=destinationCatalogClass.additernary(vdesid,feature)

    vdestidname=destinationCatalogClass.getalldestname()
    context={
        'destidnm':vdestidname,
        'quantity_range': range(1, 11)
    }
    return render(request,"additernay.html",context)