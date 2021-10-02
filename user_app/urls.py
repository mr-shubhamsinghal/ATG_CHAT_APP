from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
	path('', views.home, name='home'),
	path('register', views.register, name='register'),
	path('search-user', views.search_user, name='search-user'),
]
