from django.urls import path, URLPattern
from django.contrib.auth import views as auth_views
from . import views

urlpatterns: list[URLPattern] = [
	path('', views.index_view, name='index'),
	path('login/', auth_views.LoginView.as_view(
		template_name="login_page.html"
	), name="login")
]
