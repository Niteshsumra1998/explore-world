from django.shortcuts import render,redirect
from adddestinations.adddestimodel import destinationCatalogClass

# Create your views here.


def moredetails_view(request):
    if request.method=='POST':
        vdestid=request.POST.get("dtid")
        vpackid=request.POST.get("pkid")
        vdays=request.POST.get("vdays")
        vprice=request.POST.get("pprice")
        request.session["moredestid"]=vdestid
        request.session["morepackid"]=vpackid
        request.session["moredays"]=vdays
        request.session["moreprice"]=vprice
        return redirect('dbooknow')
    
    destinationid=request.session.get("vdestid")
    destinationname=request.session.get("vdesname")
    destinationdesc=request.session.get("vdesdesc")
    destinationimage=request.session.get("vdescimg")
    vdestf=destinationCatalogClass.getdestfeature(destinationid)
    vdestallpack=destinationCatalogClass.getalldestpackbyid(destinationid)
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    context={
        'destid':destinationid,
        'destnm':destinationname,
        'destdes':destinationdesc,
        'destimg':destinationimage,
        'dfeat':vdestf,
        'dpack':vdestallpack,
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
    }
    
    return render(request,"viewmore.html",context)