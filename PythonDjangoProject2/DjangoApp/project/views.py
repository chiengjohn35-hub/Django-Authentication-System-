from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.



@login_required
def profile(request):
    return render(request, 'profile.html')

def user_account(request):
    my_name =[{"name": "chieng", "age":18, "school":"college", "is_student":True}]
    fruits =[{
        "fruit1": "mango",
        "fruit2": "orange",
        "fruit3": "apple",
        "fruit4": "banana",
        "fruit5": "cherry",
    }]
    fruits3=["apple", "orange", "banana"]
    content = {
        "name":my_name,
        "fruits": fruits,
        "fruit2":fruits3
    }
    return render(request, 'user.html', content)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user:
            messages.info(request, "Username Already Exists!")
        else:

            new_user = User.objects.create_user(
                username=username,
                email = email
            )
            new_user.set_password(password)
            messages.success(request, "Account Successfully Created!")
            return redirect('/login/')

    return render(request, 'register.html')


def login_post(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username):
            messages.info(request, "Invalid Username!")
            return redirect('/login/')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid  Password!')
            return redirect('/login/')
        else:
            login(request, user)
            messages.success(request,'Account Successfully Logged In!')
            return redirect('profile')

    return render(request, 'login.html')


@login_required
def logout_post(request):
    logout(request)
    messages.info(request, 'Account Been Logged Out!')
    return render(request, 'logout.html')