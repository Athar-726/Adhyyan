from http import server
from django.shortcuts import get_object_or_404,render,reverse
from gc import get_objects
from django import shortcuts

from django.shortcuts import render,redirect 
from django.http import HttpResponse , JsonResponse
from account.models import *
from account.views import teacherregister 
from .models import *

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings

# Create your views here.
def index(request):
    catg = category.objects.all()
    return render(request,"home.html", {"cate":catg})
def course(request):
    cr = Service.objects.all()
    return render(request,"course.html", {"cro":cr})
def Search(request):
    dic={}
    if request.method=='GET':
        sr=request.GET['search']
        cr=Service.objects.filter(name_ser__icontains=sr)
        if len(cr)>0:
            dic['cro']=cr
        else:
            category.objects.filter(name_cat__icontains=sr)
            dic['cro']=cr 
    
    return render(request,"course.html", {"cro":cr})
def course1(request,cid):
    ctg=category.objects.get(id=cid)
    cr = Service.objects.filter(cate=ctg)
    return render(request,"course.html", {"cro":cr})
def videolect(request):
    vid=videolecture.objects.all()
    return render(request,"videolecture.html", {"video":vid})
def mock(request):
    mockt = mocktest.objects.all()
    return render(request,"profile.html", {"mt":mockt})
def Teacher(request):
    prf=profile.objects.all()
    

    return render(request,"teacher.html",{"prf":prf})
def Price (request):
    return render(request,"price.html")


def feed(request):
    dic={}
    feed=review.objects.all()
    dic['fd']=feed
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=="POST":
        rev=request.POST["review"]
        fd=review(user=usr,desc_feed=rev)
        fd.save()
        return redirect("rev")
    return render(request,"feedback.html")
def Counseling(request):
    dic={}
    usr=User.objects.all()
    dic['sf']=usr
    if request.method=="POST":
        nm=request.POST["nm"]
        mob=request.POST["cn"]
        stf=request.POST["st"]
        em=request.POST["eml"]
        tp=request.POST["tp"]
        st=get_object_or_404(User,id=stf)
        cnc=Councelingdet(name=nm,staff=st,topic=tp,mobile=mob,email=em)
        cnc.save()
        return redirect("hm")
    return render(request,"counc.html",dic)
    




def Review(request):
    re=review.objects.all()
    return render(request,"review.html",{"re":re})
    
def Contact(request):
    return render(request,"contact.html")
def Register(request):
    return render(request,"register.html")
def Register1(request):
    return render(request,"register1.html")
def Log(request):
    return render(request,"login.html")
def prof(request):
    return render(request,"profile.html")
def uprof(request):
    return render(request,"uprofile.html")
def Cart(request):
    dic={}
    item=cart.objects.filter(user_id=request.user.id,status=False)
    dic["item"]=item
    if request.user.is_authenticated:
        if request.method=="POST":
            sid=request.POST["sid"]
            quantity=request.POST["qty"]
            is_exit=cart.objects.filter(service_id=sid,user_id=request.user.id, status="False")
            if len(is_exit)>0:
                dic["msg"]="Item already exist in your cart."
            else:
                srvc=get_object_or_404(Service,id=sid)
                usr=get_object_or_404(User,id=request.user.id)
                crt=cart(user=usr,service=srvc,quantity=quantity)
                crt.save()
                dic["msg"]="{} Added in your cart.".format(Service.name_ser)
                dic["cls"]="Alert Alert Success"
        else:
            dic["status"]="Please login first to view your cart."
    return render(request, "cart.html",dic)    

def remove_ser(request):
    if "delete_cart" in request.GET:
        id=request.GET["delete_cart"]
        cartobj=get_object_or_404(cart,id=id)
        cartobj.delete()
    return HttpResponse(1)

def get_cart_data(request):
    item=cart.objects.filter(user_id=request.user.id, status=False)
    sale,quantity=0,0
    for i in item:
        sale+=float(i.service.price_ser)
        quantity=quantity+int(i.quantity)
    resp={"quan":quantity,"tot":sale}
    return JsonResponse(resp)

def process_payment(request):
    items = cart.objects.filter(user_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.service.name_ser)+"\n"
        p_ids += str(j.service.id)+","
        amt += float(j.service.price_ser)/75
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def material(request):
    mat=studymaterial.objects.all()
    return render(request,"studymaterial.html",{"cro":mat})

def add_recor(request):
    crs=Service.objects.all()
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=='POST':
        crs=request.POST['crs']
        vname= request.POST['vname']
        descrip= request.POST['descrip']
        cro=get_object_or_404(Service,id=crs)
        vid=videolecture(user=usr,service=cro,nameofvideo=vname,desc_videolecture=descrip)
        vid.save()
        if "rec_lec" in request.FILES:
            rec=request.FILES["rec_lec"]
            vid.lecture=rec
            vid.save()
    return render(request, "teacheraddlect.html",{"cro":crs})


def sgbran(request,brid):
    dic={}
    brn=Service.objects.get(id=brid)
    feeds=feedback.objects.filter(brn=brid)
    dic["feed"]=feeds
    dic["brns"]=brn
    return render(request,"review.html",dic)
def Feedback(request):
    dic={}
    usr=get_object_or_404(User,id=request.user.id)
    prf=profile.objects.get(usr_id=request.user.id)
    
    if request.user.is_authenticated:
        if request.method=='POST':
            brid=request.POST['bid']
            mes=request.POST['comments']
            rate=request.POST['rat']
            em=request.POST['email']
            br=get_object_or_404(Service,id=brid)
            fdcr=feedback(fname=usr,prf=prf,brn=br,email=em,message=mes,rating=rate)
            fdcr.save()
            return redirect('hm')

       

    return render(request,"review.html")
