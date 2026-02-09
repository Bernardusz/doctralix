# from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render

def index_view(request: HttpRequest) -> HttpResponse:
	# return render(request, 'accounts/index.html')
	return HttpResponse("Hello, this is the accounts index page.")

