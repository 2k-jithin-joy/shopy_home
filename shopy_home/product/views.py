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

#session
def pro2(request):
    s_id=request.GET['id']
    var=accessories.objects.get(id=s_id)
    if 'pre_history'in request.session:
        if s_id in request.session['pre_history']: 
            request.session['pre_history'].remove(s_id)
        pro_store=accessories.objects.filter(id__in=request.session['pre_history'])
        #pro_duct=sorted(pro_store,pro=lambda x: request.session['pre_history'].index(x.id))
        request.session['pre_history'].insert(0,s_id)
        print("STORE::",pro_store)
        if len(request.session['pre_history'])>4:
            request.session['pre_history'].pop()
        print(request.session['pre_history'])
    else:
        request.session['pre_history']=[s_id]
        pro_store=accessories.objects.filter(id=s_id)
    request.session.modified=True
    return render(request,'product.html',{'lng':var,'pro':pro_store})
    
    




def comm(request):
    user=request.GET['user']
    pro=request.GET['product']
    com=request.GET['cmd']
    users=User.objects.get(id=user)
    commnt_var=comment.objects.create(body=com,name=users.username,product_id=pro)
    commnt_var.save();
    return redirect('/product/?id='+pro)
    

    
