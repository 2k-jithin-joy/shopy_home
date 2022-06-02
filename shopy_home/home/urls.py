from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home page"),
    path('login1/',views.log,name="loginpage"),
    path('register/',views.reg),
    path('register/registersub/',views.registersub),
   
    path('logout/',views.logout)
]