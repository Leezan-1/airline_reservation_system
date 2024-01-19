# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile

def validate_alpha(value): #validates if names are only alphabets
    if not value.isalpha():
        raise ValidationError("Only alphabets are allowed.")

def validate_mobile(value): 
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("Mobile number must be a 10-digit number.")    

def validate_password(value):
    if len(value) < 8 or len(value) > 20 or not any(char in value for char in '!@#$%^&*()_+'):
        raise ValidationError("Password must be between 8 and 20 characters and contain at least one special character.")


class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True,max_length=50, validators=[validate_alpha])
    middle_name = forms.CharField(required=True,max_length=50, validators=[validate_alpha])
    last_name = forms.CharField(required=True,max_length=50, validators=[validate_alpha])
    gender = forms.ChoiceField(required=True,choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    email = forms.EmailField(required=True, max_length=50)
    mobile = forms.CharField(required=True,max_length=10, validators=[validate_mobile])
    password = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(), validators=[validate_password])
    confirm_password = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput())
    newsletter = forms.BooleanField(required=False)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if UserProfile.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("This mobile number is already in use.")
        return mobile

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,max_length=50)
    password = forms.CharField(required=True, max_length=20)

    def cleaned_email(self):
        email = self.cleaned_data.get('email')

    def cleaned_email(self):
        email = self.cleaned_data.get('email')
