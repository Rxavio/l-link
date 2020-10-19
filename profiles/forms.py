from django import forms
from .models import Profile,Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','bio', 'email','gender', 'address', 'age', 'telephone', 'nationalid','image','image2','image3')
 

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']   
 
 
class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
          