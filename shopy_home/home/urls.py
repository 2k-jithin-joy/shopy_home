from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home page"),
    path('login1/',views.log),
    path('register/',views.reg),
    path('register/registersub/',views.registersub),
    path('login1/loginsub/',views.loginsub),
    path('logout/',views.logout)
]