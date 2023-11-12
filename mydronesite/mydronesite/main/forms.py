from django import forms
from . models import CustomUser, Drone, Swarm, AP
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# creating a form

# class UserForm(forms.ModelForm):
class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    # create meta class
    class Meta:
        # specify model to be used
        model = CustomUser

        # specify fields to be used
        # fields = "__all__"
        fields = ["username", "email", "password1", "password2"]
        # exclude = ['title']

class SwarmForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Swarm

        # specify fields to be used
        # fields = "__all__"
        fields = ["swarmName"]
        # exclude = ['title']

class DroneForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Drone

        # specify fields to be used
        # fields = "__all__"
        fields = ["droneName", "IPAddress", "MAC_Address", "swarm_id"]
        # exclude = ['title']


class APForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = AP

        # specify fields to be used
        # fields = "__all__"
        fields = ["SSID", "password", "AuthMethod"]
        # exclude = ['title']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    # create meta class
    class Meta:
        # specify model to be used
        model = CustomUser

        # specify fields to be used
        fields = ["username", "email", "password1", "password2"]


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
