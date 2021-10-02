from django.urls import path

from chat_app import views

app_name = 'chat_app'

urlpatterns = [
	path('<username>', views.chat_page, name='chat'),
]
