from django.shortcuts import render,redirect
from members.forms import SignUpForm
from members.models import UserProfile

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

def login(request):
    pass