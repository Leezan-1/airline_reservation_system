# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator,RegexValidator
from .models import UserProfile
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    # this class provides validation for signup form
    first_name = forms.CharField(required=True,max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    middle_name = forms.CharField(required=True,max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    last_name = forms.CharField(required=True,max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    gender = forms.ChoiceField(required=True,choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    email = forms.EmailField(required=True, max_length=50,validators=[EmailValidator()])
    mobile = forms.CharField(required=True,max_length=10, validators=[RegexValidator(regex='^[0-9]{10}$', message='Mobile number must be 10 digits long.')])
    password = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(), validators=[
        RegexValidator(
            regex=r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]).{8,20}$',
            message='Password must be 8 to 20 characters long and contain at least 1 number and 1 symbol.'
        )
    ])
    confirm_password = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput())
    newsletter = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        # this checks if password and confirm password matches
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        # this checks if same email is used by anyone in database
        email = cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("This email is already in use.")
        
        # this checks if same mobile is used by anyone in database
        mobile = cleaned_data.get('mobile')
        if UserProfile.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("This mobile number is already in use.")
        
        return cleaned_data

    def save(self):

        mainuser = User.objects.create_user(
            username=self.cleaned_data['email'],  # Use email as the username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],  # Add first_name to the User model
            last_name=self.cleaned_data['last_name']  # Add last_name to the User model
        )


        user_profile = UserProfile.objects.create(
            user=mainuser,
            middle_name=self.cleaned_data['middle_name'],
            gender=self.cleaned_data['gender'],
            mobile=self.cleaned_data['mobile'],
            newsletter=self.cleaned_data['newsletter']
        )

        return mainuser
    


class LoginForm(forms.Form):
    # this class provides validation for login form 
    email = forms.EmailField(required=True,max_length=50, validators=[EmailValidator()])
    password = forms.CharField(required=True, max_length=20,validators=[
        RegexValidator(
            regex=r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]).{8,20}$',
            message='Password must be 8 to 20 characters long and contain at least 1 number and 1 symbol.'
        )
    ])
