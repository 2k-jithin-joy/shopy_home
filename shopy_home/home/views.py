from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from product.models import accessories

#from django.http import HttpResponse


def index(request):
    pro=accessories.objects.all()
    #print("hello",pro)
    
    return render(request,'index.html',{'pro':pro})


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
    if request.method=='POST':
        user=request.POST['uname']
        fnm=request.POST['fname']
        lnm=request.POST['lname']
        eml=request.POST['email']
        pas=request.POST['p_w']
        rep=request.POST['re-p_w']
        if user != '' and eml !='' and pas != '':
            if User.objects.filter(username=user).exists() or User.objects.filter(email=eml).exists():
                msg="username or email is already taken"
                return render(request,'register.html',{'lng':msg})
            elif pas!=rep:
                msg="password is not matching"
                return render(request,'register.html',{'lng':msg})
            else:
                userw=User.objects.create_user(username=user,first_name=fnm,last_name=lnm,email=eml,password=pas)
                userw.save();
                auth.login(request,userw)
                return redirect('/')
        else:
            msg="invalid"
            return render(request,'register.html',{'lng':msg})
    else:
        return render(request,'register.html')
    
    
     
def logout(request):
    auth.logout(request)
    return redirect("/")
    


# Create your views here.
