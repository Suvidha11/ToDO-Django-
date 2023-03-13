from django.shortcuts import render,HttpResponse,redirect
from . models import Task
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout



# Create your views here
# display task
def home(request):
    disp=Task.objects.all()
    return render(request,"index.html",{'disp': disp})

def signup(request):
    if request.method=='POST':
      username=  request.POST['username']
      email= request.POST['email']
      password= request.POST['password']
      cpassword= request.POST['cpassword']
    
      
      if password != cpassword:
        return HttpResponse('your password does not match')
      if len(password)<=4:
          return HttpResponse('your password is too short use min 4 char')
       
      add_user= User.objects.create_user(username=username, email=email,password=password)
      add_user.save()
      return redirect("login")
    
    else:
      return render(request,"signup.html")
  

def user_login(request):
    if request.method=='POST':
      username=  request.POST['username']
      password= request.POST['password']
         
      user = authenticate(username = username, password =password)
      
      if user is not None:
            login(request, user)
            request.session['user_name'] = user.username
            # print(request.session['user_name'] )
            return redirect("home")
      else: 
         return HttpResponse("inavild user and passowrd....")
    
    else:
      return render(request,"login.html")  


def hendel_logout(requset):
    logout(requset)
    return redirect("user_login")
 
#add the tasks
def add(requset):
    if requset.method == 'POST':
        task=requset.POST.get('task')
        add_task=Task(task_desc=task)
        add_task.save()    
    return redirect('home')

def delete(requset,id):
     del_task=Task.objects.get(task_id=id)
     del_task.delete()
     return redirect('home')
 
def complete(requset,id):
     cmp_task=Task.get(pk=id)
     cmp_task.status="completed"
     cmp_task.save()
     
     return redirect('home')