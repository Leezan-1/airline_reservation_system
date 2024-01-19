from django.shortcuts import render, redirect


# view that processes for sign-up.html and signup form
def index(request):
    return render(request, 'index.html')
