from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
# views.py
def home_page(request):
    information = "Welcome to Our School's Website! Here you'll find all the latest updates and announcements."
    return render(request, 'home.html', { 'information': information})
