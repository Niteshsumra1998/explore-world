from django.shortcuts import render
from .models import Package
from addpackages.addpackagemodel import packageCatalogClass
# Create your views here.

def packages_simple(request):
    package = Package.objects.all()
    vusername=request.session.get("username")
    allpackages=packageCatalogClass.getallpackages()
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    context={
        'candidatename':vusername,
        'package':package,
        'packageall':allpackages,
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
        }
    return render(request,"packages.html",context)