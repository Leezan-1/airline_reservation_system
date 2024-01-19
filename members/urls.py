from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name= 'login'),
    path("sign-up/", views.signup, name='sign-up')
]
