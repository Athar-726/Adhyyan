from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import*
from home.models import *
# Create your views here.

def register(request):
    if request.method=="POST":
        fnm=request.POST["fname"]
        lnm=request.POST["lname"]
        unm=request.POST["uname"]
        email=request.POST["email"]
        passw=request.POST["psw"]
        confpass=request.POST["cpsw"]
        con=request.POST["cn"]
        if passw==confpass:
            usr=User.objects.create_user(username=unm,first_name=fnm,last_name=lnm,email=email,password=passw)
            usr.save()
            pf=profile(usr=usr,ph_pro=con)
            pf.save()
            return redirect("lgt")
        else:
            messages.info(request, "Password not Matching")
            return redirect("reg")
    return render(request,"register.html")


def login(request):
    if request.method=="POST":
          unm=request.POST["uname"] 
          passw=request.POST["psw"]
          lg=auth.authenticate(username=unm,password=passw)
          if lg != None:
              auth.login(request,lg)
              return redirect("hm")
          else:
              return redirect("reg")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('hm')


def prof(request):
    dis={}
    pro=profile.objects.filter(usr_id=request.user.id)
    if len(pro)>0 :
        prf=profile.objects.get(usr_id=request.user.id)
        dis['prd']=prf
        mockt = mocktest.objects.all()
        dis["mt"]=mockt
    return render(request,'profile.html',dis)

def update_profile(request):
    display={}
    prof=profile.objects.filter(usr_id=request.user.id)
    if len(prof)>0:
        dis=profile.objects.get(usr_id=request.user.id)
        display["data"]=dis
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["email"]
            ph=request.POST["cno"]
            addr=request.POST["add"]
            user=User.objects.get(id=request.user.id)
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.save()
            dis.ph_pro=ph
            dis.addr_pro=addr
            dis.save()
            if "imgs" in request.FILES:
                img=request.FILES["imgs"]
                dis.img_pro=img
                dis.save()
                return redirect("pro")
                messages.info(request,"Image uploaded successfully")
            
    return render(request,"uprofile.html",display)

def teacherregister(request):
    if request.method=="POST":
        fnm=request.POST["fname"]
        lnm=request.POST["lname"]
        unm=request.POST["uname"]
        email=request.POST["email"]
        passw=request.POST["psw"]
        confpass=request.POST["cpsw"]
        con=request.POST["cn"]
        if passw==confpass:
            usr=User.objects.create_user(username=unm,first_name=fnm,last_name=lnm,email=email,password=passw)
            usr.save()
           
            if "accept" in request.POST:
                usr.is_staff=True
                usr.save()
            pf=profile(usr=usr,ph_pro=con)
            pf.save()
            messages.success(request,'CONGRATULATIONS! Your Staff details are successfully added as Trainer')
            return redirect("lgt")
        else:
            messages.info(request, "Password not Matching")
            return redirect("techregister")
    return render(request,"teacher_reg.html")