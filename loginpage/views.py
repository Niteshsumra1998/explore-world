from django.shortcuts import render,redirect
from loginpage.loginmodel import logindetails
from django.contrib import messages

# Create your views here.

def loginpage(request):
    if request.method=='POST':
        uemail=request.POST.get("useremail")
        upassword=request.POST.get("upassword")
        resultMsg=logindetails.adduserrec(uemail,upassword)
        split_message=resultMsg.split(":")
        if split_message[0]=="Error":
            messages.error(request,split_message[1])
        else:
            messageType='sucess'
            userdata=split_message[0].split("-")
            userdisplayname=userdata[1]
            userid=userdata[0]
            userrole=userdata[2]
            request.session["useremail"]=uemail
            request.session["userloginid"]=userid
            request.session["username"]=userdisplayname
            request.session["userole"]=userrole
            messages.success(request,split_message[1])

    return render(request,"loginpage.html")

def signup(request):
    return render(request, 'signup.html')
