from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def maps(request):
	return render_to_response('maps.html', context_instance = RequestContext(request))

def farmacias(request):
	return render_to_response('farmacias.html', context_instance = RequestContext(request))

def autores(request):
	return render_to_response('autores.html', context_instance = RequestContext(request))

def centrodatos(request):
	return render_to_response('centrodatos.html', context_instance = RequestContext(request))
