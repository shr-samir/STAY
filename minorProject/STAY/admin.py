from django.contrib import admin
from .models import finded_rooms
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class roomsAdmin(LeafletGeoAdmin):
 list_display=('name','coordinate','room_rate' ,'des','des')    
admin.site.register(finded_rooms,roomsAdmin)

