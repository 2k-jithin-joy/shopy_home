from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
#from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
def log(request):
    if request.method=='POST':
        user=request.POST['uname']
        pas=request.POST['p_wname']
        valid=auth.authenticate(username=user,password=pas)
        if valid is not None:
            auth.login(request,valid)
            return redirect('/')
        else:
            msg="invalid user name and password"
            return render(request,'login.html',{'lng':msg})
    else:  
        return render(request,'login.html')

def reg(request):
    print("hello",request)
    return render(request,'register.html')

def registersub(request):
    user=request.GET['uname']
    fnm=request.GET['fname']
    lnm=request.GET['lname']
    eml=request.GET['email']
    pas=request.GET['p_w']
    rep=request.GET['re-p_w']
    if user != '' and eml !='' and pas != '':
        if User.objects.filter(username=user).exists() or User.objects.filter(email=eml).exists():
            msg="username or email is already taken"
            return render(request,'register.html',{'lng':msg})
        else:
            return redirect('/')
    else:
        msg="invalid"
        return render(request,'register.html',{'lng':msg})
        
        
    
        
        
        
    
        
    print(user,fnm,lnm,eml,pas)
    return render(request,'sample.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
    


# Create your views here.
