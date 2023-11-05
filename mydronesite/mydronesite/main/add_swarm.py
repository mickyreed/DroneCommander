from django import forms
from . models import User, Drone, Swarm

# creating a form

class SwarmForm(forms.ModelForm):
    #edit_swarm = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    # create meta class
    class Meta:
        # specify model to be used
        model = Swarm

        # specify fields to be used
        fields = "__all__"
        # fields = ["swarmName"]
        # exclude = ['title']


# class DeleteSwarmForm(forms.Form):
#     delete_swarm = forms.BooleanField(widget=forms.HiddenInput, initial=True)