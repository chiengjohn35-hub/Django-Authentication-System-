from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.base import kwarg_re


#add your forms here

#Our Registration form
class RegisterForms(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()


#Our forms to display in our home(views.index) page
class PersonalForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    student = forms.BooleanField()
    school = forms.CharField()
    major = forms.CharField()
    stack = forms.CharField()







