from django.shortcuts import render,redirect
from members.forms import SignUpForm,LoginForm
from members.models import UserProfile

from django.contrib.auth import authenticate, login, logout

# Create your views here.
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
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'members/sign-up.html', {'form': form})

def login_user(request):
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
    
    return render(request, 'members/login.html', {'form':form})