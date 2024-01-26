from django.shortcuts import render, redirect
from members.forms import SignUpForm, LoginForm
from members.models import UserProfile

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signup(request):
    # this view handles signup form

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # Form is valid, save data to the database
            user = form.save()

            # Redirect to the success page upon successful completion
            return redirect('index')
        
    else:
        form = SignUpForm()

    return render(request, 'members/sign-up.html', {'form': form})


def login_user(request):
    # this view handles login form and authenticates user

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)

                # Redirect to a success page.
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'members/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('log-in')