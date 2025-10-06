from django.shortcuts import render,redirect
from .forms import RegisterForms, PersonalForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    data ={
        "name": "Chieng",
        "age": 18,
        "student": True,
        "school": "College",
        "major":"Software Engineer",
        "stack":"Full-Stack Developer",

    }

    content ={}
    content["form"]=PersonalForm(initial=data)
    return render(request, 'index.html', content)

@login_required
def profile(request):
    return render(request, 'profile.html')



#signup or register page
def register_post(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)

#use form.is_valid if submit and request method is "POST" and use "form.save()" to save user to database
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f"Account Successfully Registered!")
            return redirect('profile')
    else:
        form = RegisterForms()
    return render(request, 'register.html',{"form":form})



#login page
def login_post(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

#check and authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Account Successfully Logged In!")
            return redirect('profile')
        else:
            messages.success(request, f"Invalid Username or Password!")
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form, "title": "login"})


#logout
@login_required
def logout_post(request):
    logout(request)
    messages.info(request, 'Account Been Logged Out!')
    return render(request, 'logout.html')