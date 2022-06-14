from importlib.resources import read_binary
from django.shortcuts import render,redirect
from .models import accessories,comment

# Create your views here.
def pro(request):
    s_id=request.GET['id']
    var=accessories.objects.get(id=s_id)
    return render(request,'product.html',{'lng':var})
def comm(request):
    user=request.GET['user']
    pro=request.GET['product']
    com=request.GET['cmd']
    commnt_var=comment.objects.create(body=com,name=user,product_id=pro)
    commnt_var.save();
    return redirect('/')
    

    
