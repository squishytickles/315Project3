from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader
from models import Event
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'events/index.html')	

def detail(request, event_id):
	event = get_object_or_404(Event, id=event_id)
	user = User.objects.get(id=event.event_creator_id)
	return render(request, 'events/detail.html', {"event" : event, "owner" : user})

def create(request):
	return render(request, 'events/create.html')
	
def list(request):
	return render(request, 'events/list.html', {"events" : Event.objects.all()})
