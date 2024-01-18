from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Form is valid, save data to the database
            data = form.cleaned_data
            user_profile = UserProfile.objects.create(
                first_name=data['first_name'],
                middle_name=data['middle_name'],
                last_name=data['last_name'],
                gender=data['gender'],
                email=data['email'],
                mobile=data['mobile'],
                password=data['password'],
                newsletter=data['newsletter'],
            )
            # Redirect to the login page upon successful completion
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'sign-up.html', {'form': form})

def index(request):
    return render(request, 'index.html')
