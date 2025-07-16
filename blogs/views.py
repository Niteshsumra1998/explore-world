from django.shortcuts import render

# Create your views here.


def blogs_view(request):
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    print(vusername)
    context={
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
        }
    return render(request,"blogs.html",context)