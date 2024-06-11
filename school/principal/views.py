from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PrincipalCreationForm

def register(request):
    if request.method == 'POST':
        form = PrincipalCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = PrincipalCreationForm ()
    return render(request, 'register.html', {'form': form})


from home.views import home_page
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PrincipalLoginForm

def user_login(request):
    if request.method == 'POST':
        form = PrincipalLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or dashboard
                return redirect('home_page')
            else:
                # Invalid login
                messages.error(request, 'Invalid username or password.')
                return redirect('/principal/')
    else:
        form = PrincipalLoginForm()
    return render(request, 'login.html', {'form': form})

