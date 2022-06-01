from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
#from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
def log(request):
    return render(request,'login.html')

def reg(request):
    print("hello",request)
    return render(request,'register.html')
def loginsub(request):
    user=request.GET['uname']
    pas=request.GET['p_wname']
    valid=auth.authenticate(username=user,password=pas)
    if valid is not None:
        auth.login(request,valid)
        return redirect('/')
    else:
        msg="invalid user name and password"
        return render(request,'login.html',{'lng':msg})
def registersub(request):
    return render(request,'sample.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
    


# Create your views here.
