from django.contrib import admin
from .models import User, Drone, Swarm


class UserAdmin(admin.ModelAdmin): # we insert these two lines…
   list_display = ('userName', 'email') # list the fields we want on the list display

class DroneAdmin(admin.ModelAdmin): # we insert these two lines…
   list_display = ('droneName', 'user_id') # list the fields we want on the list display

# class SwarmAdmin(admin.ModelAdmin): # we insert these two lines…
#    list_display = ('swarmName') # list the fields we want on the list display


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Drone, DroneAdmin)
admin.site.register(Swarm)
