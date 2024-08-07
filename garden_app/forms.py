from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import GardeningGroup, Upload
from .models import Post
from .models import Profile

class UserRegisterForm(UserCreationForm): #rosh
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): #rosh
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'required': 'required'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': 'required'
    }))


class ProfileForm(forms.ModelForm): #yash
    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'location']

class GroupPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']

class GardeningGroupForm(forms.ModelForm): #smit
    class Meta:
        model = GardeningGroup
        fields = ['name', 'description', 'image']

class UploadForm(forms.ModelForm): #smit
    class Meta:
        model = Upload
        fields = ['photo', 'tip']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'required': False}),
        }

class UploadForm(forms.ModelForm): #smit
    class Meta:
        model = Upload
        fields = ['photo', 'tip']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'required': False}),
        }

class GardeningGroupForm(forms.ModelForm): #smit
    class Meta:
        model = GardeningGroup
        fields = ['name', 'description', 'image']