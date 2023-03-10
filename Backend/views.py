from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb,admindb
from Frontend.models import savecontactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def loginpage(request):
    return render(request,"loginpage.html")
def adminloginpage(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')

        if User.objects.filter(username__contains=username_a).exists():
            user=authenticate(username=username_a,password=password_a)
            if user is not None:
                login(request,user)
                request.session['username']=username_a
                request.session['password']=password_a

                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def indexpage(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request,"admin.html")
def saveadmin(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        USERNAME = req.POST.get('username')
        PASSWORD = req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('conpassword')
        IMAGE = req.FILES['image']
        obj=admindb(Name=NAME,Username=USERNAME,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Email=EMAIL,Image=IMAGE)
        obj.save()
        return redirect(adminpage)
def viewadmin(request):
    data=admindb.objects.all()
    return render(request,"viewadmin.html",{'data':data})
def editadmin(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,"editadmin.html",{'data':data})
def updateadmin(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        EMAIL = req.POST.get('email')
        USERNAME = req.POST.get('username')
        PASSWORD = req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('conpassword')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(Name=NAME,Username=USERNAME,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Email=EMAIL,Image=file)
        return redirect(viewadmin)


def deleteadmin(request,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewadmin)

def categorypage(request):
    return render(request,"category.html")
def viewcategory(request):
    data=categorydb.objects.all()
    return render(request,"viewcategory.html",{'data':data})
def savecategory(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        DESCRIPTION=req.POST.get('description')
        IMAGE = req.FILES['image']
        obj=categorydb(Name=NAME,Description=DESCRIPTION,Image=IMAGE)
        obj.save()
        return redirect(categorypage)

def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,"editcategory.html",{'data':data})


def updatecategory(request,dataid):
    if request.method=="POST":
        NAME = request.POST.get('name')
        DESCRIPTION = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=NAME, Description=DESCRIPTION, Image=file)
        return redirect(viewcategory)

def deletecategory(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcategory)


def addproduct(request):
    data =categorydb.objects.all()
    return render(request,"product.html",{'data':data})
def saveproduct(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        PRICE=req.POST.get('price')
        DESCRIPTION=req.POST.get('description')
        QUANTITY = req.POST.get('quantity')
        CATEGORY = req.POST.get('category')
        IMAGE = req.FILES['image']
        obj=productdb(Name=NAME,Price=PRICE,Description=DESCRIPTION,Quantity=QUANTITY,Category=CATEGORY,Image=IMAGE)
        obj.save()
        return redirect(addproduct)
def viewproductB(request):
    data=productdb.objects.all()
    return render(request,"viewproduct.html",{'data':data})
def editproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    print(da)
    return render(request,"editproduct.html",{'datas':data,'da':da})
def updateproduct(request,dataid):
    if request.method=="POST":
        NAME = request.POST.get('name')
        PRICE = request.POST.get('price')
        DESCRIPTION = request.POST.get('description')
        QUANTITY = request.POST.get('quantity')
        CATEGORY = request.POST.get('category')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Name=NAME, Description=DESCRIPTION,Price=PRICE,Quantity=QUANTITY,Category=CATEGORY, Image=file)
        return redirect(viewproductB)
def deleteproduct(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewproductB)
def viewcomplaint(request):
    data=savecontactdb.objects.all()
    return render(request,"viewcomplaint.html",{'data':data})
def deletecomplaint(request,dataid):
    data=savecontactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcomplaint)










