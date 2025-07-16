from django.shortcuts import render

def home(request):
    #request.session["username"]=""
    vusername=request.session.get("username")
    vuserid=request.session.get("userloginid")
    vuserole=request.session.get("userole")
    print(vusername)
    context={
        'candidatename':vusername,
        'userid':vuserid,
        'userrole':vuserole
        }
    return render(request, 'home.html',context)
