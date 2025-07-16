from django.shortcuts import render,redirect
from adddestinations.adddestimodel import destinationCatalogClass

# Create your views here.

def destionations(request):
    if request.method=="POST":
        request.session["vdestid"]=request.POST.get("desid")
        request.session["vdesname"]=request.POST.get("desnm")
        request.session["vdesdesc"]=request.POST.get("desd")
        request.session["vdescimg"]=request.POST.get("desim")
        
        return redirect('moredetails_view')
    vusername=request.session.get("username")
    search_query = request.GET.get("q", "")
    if search_query:
        alldestinations = destinationCatalogClass.getdestinationbysearch(search_query)
    else:
        alldestinations = destinationCatalogClass.getalldestinations()
    
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    #print(vusername)

    context={
        'candidatename':vusername,
        'destall':alldestinations,
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
        }
    return render(request,"destionations.html",context)