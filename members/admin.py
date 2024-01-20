from django.contrib import admin
from members.models import UserProfile
# Register your models here.

admin.site.register(UserProfile) #shows UserProfile database in admin portal and can be editable in it
