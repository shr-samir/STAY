from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def signin(request):
    if request.method=="POST":
       firstname=request.POST['first_name'] 
       lastname=request.POST['last_name'] 
       username=request.POST['user_name'] 
       Email=request.POST['email'] 
       password_1=request.POST['password1'] 
       password_2=request.POST['password2'] 
       
       if password_1==password_2:
          if User.objects.filter(username=username).exists():#to check from database wheather this username already exists or not 
            messages.info(request,"Username already taken")
            return redirect('signin')            
          elif User.objects.filter(email=Email).exists():#to check from database wheather this email already exists or not 
            messages.info(request,"Email already taken") 
            return redirect('signin')               
          else:        
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password_1,email=Email)#(here field names should be same as in database)
            user.save()# entered data are saved in database
            messages.info(request,"New user created") 
            return redirect('login')      
       else:
          messages.info(request,"Password didn't match")  
          return redirect('signin')
    else:
     return render(request,'signin.html')
  
def login(request):
 if request.method=="POST": 
       username=request.POST['user_name']    
       password_1=request.POST['password1'] 
       user=auth.authenticate(username=username,password=password_1)
       if user is not None:
         auth.login(request,user)
         return redirect('/')
       else:
         messages.info(request,"Invalid credentials")
         return redirect('login')
 else:
    return render(request,'login.html')
  
def logout(request):
  auth.logout(request)
  return redirect('/')#takes back to base.html(home) page