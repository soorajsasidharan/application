from django import forms 
from .models import Home, Profile

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Home 
        fields = ['username','post_image', 'caption'] 

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['profile_image', 'bio']

