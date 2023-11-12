from django.contrib import admin
from .models import CustomUser, Drone, Swarm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(admin.ModelAdmin): # we insert these two lines…
   list_display = ('username', 'email') # list the fields we want on the list display

class DroneAdmin(admin.ModelAdmin): # we insert these two lines…
   list_display = ('droneName', 'user_id') # list the fields we want on the list display

class SwarmAdmin(admin.ModelAdmin): # we insert these two lines…
   list_display = ('swarmName', 'user_id') # list the fields we want on the list display


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Drone, DroneAdmin)
admin.site.register(Swarm, SwarmAdmin)
