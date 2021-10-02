from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from user_app.models import captchaModel

from user_app.forms import UserRegisterForm
from user_app import utils

def home(request):
	context = {'homepage_error': ''}
	return render(request, 'home/homepage.html', context)


def register(request):
	captcha_valid = True
	if request.method == 'POST':
		data = request.POST.get('captcha_challenge')
		res = request.POST.get('captcha_result')
		expected_result = captchaModel.objects.get(captcha_string=data)
		form = UserRegisterForm(request.POST)
		if expected_result.captcha_res == res:
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=raw_password)
				login(request, user)
				return redirect('user_app:home')
		else:
			captcha_valid = False
	else:
		form = UserRegisterForm()
	captcha = utils.get_captcha()

	error_msg = ''

	if not captcha_valid:
		error_msg = 'Invalid Captcha'

	context = {
			'form': form, 'captcha': captcha,
			'error_msg': error_msg
		}

	return render(request, 'home/register.html', context)


def search_user(request):
	try:
		username = request.POST.get('username')
		second_user = User.objects.get(username=username)
	except User.DoesNotExist:
		context = {'homepage_error': username + ' username does not exist'}
		return render(request, 'home/homepage.html', context)
	context = {'second_username': username}
	return render(request, 'chat/chat_page.html', context)
