from django import forms
from .models import Thing, Category, Page, UserProfile
from django.contrib.auth.models import User

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

#import floppyforms as forms
#from .models import Thing


#class ThingForm(forms.ModelForm):
#    class Meta:
#        model = Thing

class UserForm(forms.ModelForm):
    #from django.contrib.auth.models import User
    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)