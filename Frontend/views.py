from django.shortcuts import render,redirect
from django.contrib import messages


from Backend.models import categorydb,productdb
from Frontend.models import registrationdb,savecontactdb


# Create your views here.
def loginfront(request):
    if request.method=='POST':
        username_r=request.POST.get("usernamel")
        password_r = request.POST.get("passwordl")
        if registrationdb.objects.filter(Name=username_r,Password=password_r).exists():
            request.session['usernamel']=username_r
            request.session['passwordl'] = password_r
            messages.success(request,"Login Successfully")
            return redirect(homehtmlpage)
        else:
            messages.error(request, "Invalid User")
            return render(request,'registration.html',{'msg':"sorry...invalid username or password"})

def logoutfront(request):
    del request.session['usernamel']
    del request.session['passwordl']
    return redirect(registration)

def homehtmlpage(request):
    data = categorydb.objects.all()
    return render(request,"home.html",{'data':data})
def aboutus(request):
    return render(request,"about.html")
def registration(request):
    return render(request,"registration.html")
def saveregistration(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        PASSWORD=req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('confirmpassword')
        obj=registrationdb(Name=NAME,Email=EMAIL,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD)
        obj.save()
        messages.success(req,"Registered Successfully")
        return redirect(registration)
def contact(request):
    return render(request,"contact.html")
def savecontact(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        SUBJECT=req.POST.get('subject')
        MESSAGE=req.POST.get('message')
        obj=savecontactdb(Name=NAME,Email=EMAIL,Subject=SUBJECT,Message=MESSAGE)
        obj.save()
        return redirect(contact)
def viewproducts(request,itemcatg):
    print("====itemcatg====",itemcatg)
    catg=itemcatg.upper()
    products=productdb.objects.filter(Name=itemcatg)
    context={
        'products':products,
        'catg':catg
    }
    return render(request,"viewproductsF.html",context)
def singleproduct(request,dataid):
    data= productdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'dat':data})
