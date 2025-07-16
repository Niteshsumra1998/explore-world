from django.shortcuts import render,redirect
from adddestinations.adddestimodel import destinationCatalogClass
# Create your views here.

def dbooknow(request):
    vardid=request.session.get("moredestid")
    varpackid=request.session.get("morepackid")
    varpdays=request.session.get("moredays")
    varprice=request.session.get("moreprice")
    print(varpdays)
    print(varprice)
    if request.method=='POST':
     vtel=request.POST.get("ttel")
     vadd=request.POST.get("tadd")
     vpassenger=request.POST.get("quantity")
     vjdate=request.POST.get("journeyDate")
     vjend=request.POST.get("journeyEndDate")
     vtotal=request.POST.get("totalAmount")
     vuserid=request.session.get("userloginid")
     splitvalue=vtotal.split(" ")
     request.session["tamount"]=int(splitvalue[1])
     vbookingid=destinationCatalogClass.savebookingdetails(vuserid,vtel,vadd,vpassenger,vardid,varpackid,vjdate,vjend,splitvalue[1])
     vqty=int(request.POST.get("quantity"))
     for i in range(1, vqty + 1):
        pname = request.POST.get(f"passengerName{i}")
        page = request.POST.get(f"passengerAge{i}")
        vresult=destinationCatalogClass.savetravellerdetails(vbookingid,pname,page)
     print(vbookingid)
     print(vresult)
     request.session["telno"]=vtel
     request.session["bookingids"]=vbookingid
     return redirect('razorpay_views')
    context={
         'quantity_range': range(1, 11),
         'did':vardid,
         'packid':varpackid,
         'pdays':varpdays,
         'pricep':varprice
     }
    
    return render(request,"dbooknow.html",context)