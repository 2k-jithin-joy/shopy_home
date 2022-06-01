from urllib import request
from django.shortcuts import render
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
    print("hell",user)
    print("hell",pas)
    return render(request,'sample.html')
def registersub(request):
    return render(request,'sample.html')


# Create your views here.
