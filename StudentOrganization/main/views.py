from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	output = "Hello, "
	if request.user.is_authenticated():
		output += request.user.first_name
	else:
		output += "world"
	return HttpResponse(output)
