from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
            messages.add_message(request, messages.SUCCESS, 'Successfully created user.')
        else:
            messages.add_message(request, messages.ERROR, "One or more fields in the form is incorrect. Please review.")
    else:
        form = RegisterForm()
        
    return render(request, "sign_up.html", {
        "title": "Sign Up", 
        "form": form,
        })


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.add_message(request, messages.SUCCESS, f'Authenticated as {username}.')
            return redirect('/user_dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Couldn't verify credentials. Please review your fields.")
            return redirect('log_in')

    return render(request, "log_in.html", {
        "title": "Log In",
        })