from django.urls import path,include
from home import views

from product.feed import feed_pro

urlpatterns = [
    path('',views.index,name="home page"),
    path('login1/',views.log,name="loginpage"),
    path('register/',views.reg,name="regpage"),
    path('logout/',views.logout),
    path('search/',views.search,name="searching"),
    path('feed/',feed_pro(),name='feed'),
    path('sign/',views.sign)
    
]