from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name= 'log-in'),
    path("log-out/", views.login_user, name= 'log-out'),
    path("sign-up/", views.signup, name='sign-up')
]
