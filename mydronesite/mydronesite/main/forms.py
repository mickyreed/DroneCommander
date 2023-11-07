from django import forms
from . models import User, Drone, Swarm

# creating a form
class UserForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = "__all__"
        # fields = ["userName", "email"]
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
        fields = ["droneName", "IPAddress"]
        # exclude = ['title']
