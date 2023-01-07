from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.

class finded_rooms(models.Model):
    name=models.CharField(max_length=20)
    coordinate=models.PointField(srid=4326)
    room_rate=models.IntegerField()
    des=models.TextField() 
    objects = GeoManager()

class listedRooms(models.Model):

    ROOMTYPES = (
        ('EF', 'Entire Flat'),
        ('SR', 'Shared Room'),
        ('PR', 'Private Room')
    )

    location=models.CharField(max_length=100)

    roomType=models.CharField(max_length=15, choices=ROOMTYPES, default="EF") 
    bedrooms=models.IntegerField(max_length=12) 
    bathrooms=models.IntegerField(max_length=12)  
    occupants=models.IntegerField(max_length=12)  
    
    phoneNum=models.IntegerField(max_length=10)  

    rent=models.rent 

    furnished=models.BooleanField(default=False)
    wifiIncluded=models.BooleanField(default=False) 
    privateBathroom=models.BooleanField(default=False) 
    hasDogs=models.BooleanField(default=False) 
    water24hr=models.BooleanField(default=False) 
    rooftopAccess=models.BooleanField(default=False) 
    ac=models.BooleanField(default=False) 
    hasCats=models.BooleanField(default=False) 
    balcony=models.BooleanField(default=False) 
    outdoorSpace=models.BooleanField(default=False) 
    utilitiesIncluded=models.BooleanField(default=False) 
    hasOtherPets=models.BooleanField(default=False) 
    bikeParking=models.BooleanField(default=False)
    carParking=models.BooleanField(default=False)

    noSmoking=models.BooleanField(default=False) 
    noLateNights=models.BooleanField(default=False) 
    dogsOK=models.BooleanField(default=False) 
    noPets=models.BooleanField(default=False) 
    noDrinking=models.BooleanField(default=False) 
    noFriends=models.BooleanField(default=False) 
    catsOK=models.BooleanField(default=False)
    otherPetsOK=models.BooleanField(default=False)

    desc=models.BooleanField(default=False)   

	

def __unicode__(self):                #constructor
        return self.name
