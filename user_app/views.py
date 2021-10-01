from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from user_app.forms import UserRegisterForm


def home(request):
	return render(request, 'home/homepage.html')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('user_app:home')
	else:
		form = UserRegisterForm()
	return render(request, 'home/register.html', {'form': form})
