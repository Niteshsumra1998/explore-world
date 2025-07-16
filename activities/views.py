from django.shortcuts import render

# Create your views here.
def activities_views(request):
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    context={
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
        }
    return render(request,"activities.html",context)