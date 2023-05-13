from django import forms
from base.models import Profile
from django.contrib.auth.models import User



class ProfileAvatarForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("avatar", )
