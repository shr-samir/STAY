from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import finded_rooms
from django.contrib.gis.geos import Point
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

#Shows directly homepage
class base(TemplateView):
    template_name= 'base.html'

def rooms_datasets(request):    
   rooms = serialize('geojson', finded_rooms.objects.all())  
   return HttpResponse(rooms,content_type='json')

def showrooms(request):
    return render(request,'index.html')

def helpp(request):
    return render(request,'help.html')

def listingForm(request):
    if request.method=="POST":

        if User.objects.filter(email=Email).exists():

            location=request.POST['location']  

            roomType=request.POST['roomType'] 
            bedrooms=request.POST['bedrooms'] 
            bathrooms=request.POST['bathrooms'] 
            occupants=request.POST['occupants'] 
            
            phoneNum=request.POST['phoneNum'] 

            rent=request.POST['rent'] 

            furnished=request.POST['furnished'] 
            wifiIncluded=request.POST['wifiIncluded'] 
            privateBathroom=request.POST['privateBathroom'] 
            hasDogs=request.POST['hasDogs'] 
            water24hr=request.POST['water24hr'] 
            rooftopAccess=request.POST['rooftopAccess'] 
            ac=request.POST['ac'] 
            hasCats=request.POST['hasCats'] 
            balcony=request.POST['balcony'] 
            outdoorSpace=request.POST['outdoorSpace'] 
            utilitiesIncluded=request.POST['utilitiesIncluded'] 
            hasOtherPets=request.POST['hasOtherPets'] 
            bikeParking=request.POST['bikeParking']
            carParking=request.POST['carParking']

            noSmoking=request.POST['noSmoking'] 
            noLateNights=request.POST['noLateNights'] 
            dogsOK=request.POST['dogsOK'] 
            noPets=request.POST['noPets'] 
            noDrinking=request.POST['noDrinking'] 
            noFriends=request.POST['noFriends'] 
            catsOK=request.POST['catsOK']
            otherPetsOK=request.POST['otherPetsOK']

            desc=request.POST['desc']

        


            user=User.objects.create_user(location=location,roomType=roomType,bedrooms=bedrooms,bathrooms=bathrooms,occupants=occupants,phoneNum=phoneNum,rent=rent,furnished=furnished,wifiIncluded=wifiIncluded,privateBathroom=privateBathroom,hasDogs=hasDogs,water24hr=water24hr,rooftopAccess=rooftopAccess,ac=ac,hasCats=hasCats,balcony=balcony,outdoorSpace=outdoorSpace,utilitiesIncluded=utilitiesIncluded,hasOtherPets=hasOtherPets,bikeParking=bikeParking,carParking=carParking,noSmoking=noSmoking,noLateNights=noLateNights,dogsOK=dogsOK,noPets=noPets,noDrinking=noDrinking,noFriends=noFriends,catsOK=catsOK,otherPetsOK=otherPetsOK,desc=desc) 

            user.save()# entered data are saved in database
            messages.info(request,"New user created") 
        return redirect('login')

    else:
        return render(request,'listingForm.html')
          
