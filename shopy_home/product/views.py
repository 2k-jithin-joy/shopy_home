from importlib.resources import read_binary
from django.shortcuts import render,redirect
from .models import accessories,comment
from django.contrib.auth.models import User
from django.core.cache import cache
# Create your views here.
def pro(request):
    s_id=request.GET['id']
    if cache.get(s_id):
        
        print("DATA FROM CACHE")
        var=cache.get(s_id)
        print(var)
    else:
        print("DATA FROM DATABASE")
        var=accessories.objects.get(id=s_id)
        cache.set(s_id,var)
    return render(request,'product.html',{'lng':var})




def comm(request):
    user=request.GET['user']
    pro=request.GET['product']
    com=request.GET['cmd']
    users=User.objects.get(id=user)
    commnt_var=comment.objects.create(body=com,name=users.username,product_id=pro)
    commnt_var.save();
    return redirect('/product/?id='+pro)
    

    
