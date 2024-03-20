from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import UserProfile, User, Item 
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request, 'home.html')

def user_profile_list(request):
    profiles= UserProfile.objects.all()
    return render(request, 'base.html', {'profiles': profiles})

@login_required
def items_list(request):
    items=Item.objects.all()
    return render(request, 'staff.html', {'items': items})


def log_out(request):
    logout(request)
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            if user is not None:
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff: 
                login(request, user)
                return redirect('staff')
            else: 
                login(request, user)
                return redirect('home')

        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    




import random 


def generate_random_users(num_users):
    for _ in range(num_users):
       username=f'user_{random.randint(1000, 9999)}'
       first_name=f'user_{random.randint(1000, 9999)}'
       last_name=f'user_{random.randint(1000, 9999)}'
       email=f'user_{random.randint(1000, 99999)}@abc.com'
       password=f'password_{random.randint(1000, 9999)}'

       user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
       user.save 
