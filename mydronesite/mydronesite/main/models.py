import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import DateTimeField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have a valid email address")
        if not username:
            raise ValueError("User must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),  # normalize as lowercase
            username=username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


# Create your models here.
# class User(models.Model):
#
#     # userID=models.IntegerField(unique=True)
#     userName=models.CharField(max_length=32,unique=True)
#     email=models.EmailField(unique=True,max_length=64)
#
#     def __str__(self):
#         return self.userName or ' '


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(_("email address"),max_length=64, unique=True)
    date_joined=models.DateTimeField("dateJoined", default=timezone.now)
    last_login: DateTimeField = models.DateTimeField("lastLogin",auto_now=True)
    is_super_user = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # hide_email = models.BooleanField(default=True)  # comment this if i want to use username
    # hide_password = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'  # comment this if i want to use username
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Swarm(models.Model):
    # swarmID=models.IntegerField(unique=True)
    swarmName=models.fields.CharField(max_length=32,unique=True)
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    createdAt=models.DateTimeField("datePublished", default=timezone.now)
    UpdatedAt=models.DateTimeField("dateUpdated", auto_now=True)
    UpdatedBy=models.CharField(max_length=32, default="User")

    def __str__(self):
        return self.swarmName or ''


class Drone(models.Model):
    user_id=models.ForeignKey(CustomUser,null=True, on_delete=models.SET_NULL)
    droneName=models.fields.CharField(max_length=32,unique=True)
    MAC_Address=models.CharField(max_length=17, default="00-00-00-00-00-00")
    IPAddress=models.GenericIPAddressField(max_length=64, default="192.168.1.1")
    createdAt=models.DateTimeField("datePublished", default=timezone.now)
    swarm_id=models.ForeignKey(Swarm,null=True, blank=True, on_delete=models.SET_NULL)
    UpdatedBy=models.CharField(max_length=32, default="User")

    def __str__(self):
        return self.droneName or ''


class AP(models.Model):
    # APID=models.IntegerField(max_length=1, default=1, unique=True)
    SSID=models.fields.CharField(max_length=32,unique=True)
    password=models.fields.CharField(max_length=32, default='1234')
    AuthMethod=models.fields.CharField(max_length=16, default='EAP')
    CreatedAt = models.DateTimeField("datePublished", default=timezone.now)
    UpdatedAt = models.DateTimeField("dateUpdated", auto_now=True)
    UpdatedBy = models.CharField(max_length=32, default="User")
