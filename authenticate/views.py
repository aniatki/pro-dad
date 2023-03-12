from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created user.')
        else:
            messages.success(request, 'Please review the details you provided.')
    else:
        form = RegisterForm()
        
    return render(request, "sign_up.html", {
        "title": "Sign Up", 
        "form": form, 
        'messages': messages
        })


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Successfully logged in.')
            return redirect('/user_dashboard')
        else:
            messages.success(request, "There seems to be a problem logging in.")
            return redirect('log_in')

    return render(request, "log_in.html", {
        "title": "Log In", 
        'messages': messages
        })