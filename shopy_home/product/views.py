from importlib.resources import read_binary
from django.shortcuts import render
from .models import accessories

# Create your views here.
def pro(request):
    s_id=request.GET['id']
    var=accessories.objects.get(id=s_id)
    return render(request,'product.html',{'lng':var})
    
