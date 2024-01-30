from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name= 'log-in'), # members/
    path("log-out/", views.logout_user, name= 'log-out'), # members/log-out
    path("sign-up/", views.signup, name='sign-up'), # members/sign-up
    path("edit-profile/", views.edit_profile, name='edit-profile') # members/sign-up
]
