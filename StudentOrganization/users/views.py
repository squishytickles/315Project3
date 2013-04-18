from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return HttpResponse("Users Index")

def detail(request, user_id):
	user = get_object_or_404(User, id=user_id)
	return render(request, 'users/detail.html', {"user" : user})
