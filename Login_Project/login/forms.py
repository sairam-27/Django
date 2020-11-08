from django import forms
from django.contrib.auth.models import User
from login.models import userProfile

class userForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class userProfileForm(forms.ModelForm):


    class Meta():
        model = userProfile
        fields = ('LinkedInSite', 'profile_pic')
