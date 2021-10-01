from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
	path('', views.home, name='home'),
]
