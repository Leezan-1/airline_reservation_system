from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    middle_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    last_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[A-Za-z]*$', message='Only alphabets are allowed.')])
    gender = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    email = models.EmailField(max_length=50,unique=True, validators=[EmailValidator()])
    mobile = models.CharField(unique=True, max_length=10, validators=[RegexValidator(regex='^[0-9]{10}$', message='Mobile number must be 10 digits long.')])
    password = models.CharField(max_length=20,validators=[RegexValidator(
        regex=r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]).{8,20}$',
        message='Password must be 8 to 20 characters long and contain at least 1 number and 1 symbol.'
    )
])

    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

