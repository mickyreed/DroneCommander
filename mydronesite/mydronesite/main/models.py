from django.db import models


# Create your models here.
class User(models.Model):

    # userID=models.IntegerField(unique=True)
    userName=models.CharField(max_length=32,unique=True)
    email=models.EmailField(unique=True,max_length=64)

    def __str__(self):
        return self.userName or ' '


class Swarm(models.Model):
    # swarmID=models.IntegerField(unique=True)
    swarmName=models.fields.CharField(max_length=32,unique=True)
    # createdAt=models.DateTimeField("datePublished")
    # UpdatedAt=models.DateTimeField("dateUpdated")
    # UpdatedBy=models.IntegerField()

    def __str__(self):
     return self.swarmName or ' '


class Drone(models.Model):
    user_id=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    droneName=models.fields.CharField(max_length=32,unique=True)
    # MAC_Address=models.CharField(max_length=17)
    # IPAddress=models.GenericIPAddressField(max_length=64)
    # createdAT=models.DateTimeField("datePublished")
    # swarm_id=models.ForeignKey(Swarm,null=True, blank=True, on_delete=models.SET_NULL)
    # updatedBy=models.IntegerField()

    def __str__(self):
        return self.droneName or ' '
