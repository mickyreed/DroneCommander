from django import forms
from . models import User, Drone, Swarm

# creating a form

class DroneForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Drone

        # specify fields to be used
        fields = "__all__"
        # fields = ["droneName"]
        # exclude = ['title']




# class DeleteSwarmForm(forms.Form):
#     delete_swarm = forms.BooleanField(widget=forms.HiddenInput, initial=True)