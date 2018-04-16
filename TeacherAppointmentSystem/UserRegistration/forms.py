from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserRegistration.models import User
from django.contrib.auth import authenticate


class StudentSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['varsity_id','user_mail','username']



class TeacherSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['varsity_id','user_mail','teacher_initial','username']




class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

