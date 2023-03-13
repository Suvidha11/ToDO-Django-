from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
 path('add',views.add, name="add"),
 path('',views.signup, name="signup"),  
 path('user_login',views.user_login, name="user_login"), 
 path('hendel_logout/',views.hendel_logout, name="hendel_logout"),     
 path('home',views.home, name="home"), 
 path('delete/<int:id>',views.delete, name="delete"),  
  path('complete/<int:id>',views.complete, name="complete"),  
   
]