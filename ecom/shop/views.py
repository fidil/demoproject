from django.shortcuts import render,redirect
from shop.models import Product,Category
# from books import views
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


def home(requset):
    c=Category.objects.all()

    return render(requset,'category.html',{'c':c})


def allproducts(requset,p):
    c=Category.objects.get(slug=p)
    product=Product.objects.filter(category__slug=p)
    return render(requset,'products.html',{'product':product,'c':c})

def prodetail(request,p):
    p=Product.objects.get(slug=p)
    return render(request,'detail.html',{'p':p})


def regitr(request):
    if(request.method=="POST"):
        u=request.POST["u"]
        p=request.POST["p"]
        cp=request.POST["cp"]
        e=request.POST["e"]
        f=request.POST["f"]
        l=request.POST["l"]
        if(cp==p):
            u=User.objects.create_user(username=u,
                                       password=p,
                                       email=e,
                                       first_name=f,
                                       last_name=l)
            u.save()
            return redirect('shop:home')
        else:
            messages.error(request, "PASSWORDS ARE NOT SAME")

    return render(request,'regitr.html')

def user_login(request):
    if(request.method=="POST"):
        username=request.POST['u']
        password=request.POST['p']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            messages.error(request,"invalid user credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:home')
