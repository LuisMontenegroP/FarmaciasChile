from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from FarmaciasChile.models import Farmacias

# Create your views here.

def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def maps(request):
	farmacias_select = Farmacias.objects.all()
	return render_to_response('maps.html', {'farmacias_select': farmacias_select}, context_instance = RequestContext(request))

def acercade(request):
	return render_to_response('acercade.html', context_instance = RequestContext(request))

def farmacias(request):
	return render_to_response('farmacias.html', context_instance = RequestContext(request))

def autores(request):
	return render_to_response('autores.html', context_instance = RequestContext(request))

def centrodatos(request):
	farmacias = Farmacias.objects.all()
	return render_to_response('centrodatos.html', {'farmacias': farmacias}, context_instance = RequestContext(request))
