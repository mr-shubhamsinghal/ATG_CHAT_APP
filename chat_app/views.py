from django.shortcuts import render

# Create your views here.
def chat_page(request, username):
	context = {'username': username}
	return render(request, 'chat/chat_page.html', context)
