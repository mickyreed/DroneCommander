import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(models.Model):

    # userID=models.IntegerField(unique=True)
    userName=models.CharField(max_length=32,unique=True)
    email=models.EmailField(unique=True,max_length=64)

    def __str__(self):
        return self.userName or ' '

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email

class Swarm(models.Model):
    # swarmID=models.IntegerField(unique=True)
    swarmName=models.fields.CharField(max_length=32,unique=True)
    # createdAt=models.DateTimeField("datePublished",default=datetime.datetime)
    # UpdatedAt=models.DateTimeField("dateUpdated", default=datetime.datetime)
    # UpdatedBy=models.IntegerField(default=" ")

    def __str__(self):
        return self.swarmName or ' '


class Drone(models.Model):
    user_id=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    droneName=models.fields.CharField(max_length=32,unique=True)
    MAC_Address=models.CharField(max_length=17, default="00-00-00-00-00-00")
    IPAddress=models.GenericIPAddressField(max_length=64, default="192.168.1.1")
    # createdAT=models.DateTimeField("datePublished",default=datetime.datetime)
    # swarm_id=models.ForeignKey(Swarm,null=True, blank=True, on_delete=models.SET_NULL)
    # updatedBy=models.IntegerField(default=" ")

    def __str__(self):
        return self.droneName or ' '
