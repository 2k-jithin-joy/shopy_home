from django.urls import path,include
from product import views


urlpatterns = [
    
    path('',views.pro2),
    path('comment/',views.comm),


]