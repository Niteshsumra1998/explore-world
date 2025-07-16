from django.shortcuts import render
from registrations.usermodule import userrecord
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.contrib import messages
# Create your views here.


def userview(request):
    if request.method=='POST':
        usernm=request.POST.get('username')
        useremail=request.POST.get('email')
        userpassword=request.POST.get('password')

        message=userrecord.adduserrecord(usernm,useremail,userpassword)
        split_message=message.split(":")
        if split_message[0]!="Error":
            send_mail(
                subject='test',
                message=('Hello welcome to test key. \n This is a testing feild'),
                from_email=('ExploreIndia'),
                recipient_list=[useremail],
                fail_silently=False,
            )
            messages.success(request,split_message[1])
        else:
            messages.error(request,split_message[0])
        #return HttpResponse(message)
    return render(request,"signup.html")