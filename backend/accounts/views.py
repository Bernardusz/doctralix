from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.

def index_view(request: HttpRequest) -> HttpResponse:
	return render(request, 'index.html')

def login_page(request: HttpRequest) -> HttpResponse:
	return render(request, 'login_page.html')