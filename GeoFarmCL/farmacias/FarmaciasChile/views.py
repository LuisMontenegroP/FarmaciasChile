from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from FarmaciasChile.models import Farmacias
from django.db.models import Count


def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def acercade(request):
	return render_to_response('acercade.html', context_instance = RequestContext(request))

def farmacias(request):
	farmacias = Farmacias.objects.all()
	return render_to_response('farmacias.html', {'farmacias': farmacias}, context_instance = RequestContext(request))

def autores(request):
	return render_to_response('autores.html', context_instance = RequestContext(request))

def conclusiones(request):
	return render_to_response('conclusiones.html', context_instance = RequestContext(request))

def centrodatos(request):
	farmacias = Farmacias.objects.all()
	return render_to_response('centrodatos.html', {'farmacias': farmacias}, context_instance = RequestContext(request))

def maps(request):
	#farmacias = Farmacias.objects.filter(local_nombre = 'FARMACIAS CRUZ VERDE')
	farmacias = Farmacias.objects.all()
   	farmacias_select = Farmacias.objects.values('local_nombre').annotate(dcount=Count('local_nombre'))
	medicamentos_select = Farmacias.objects.exclude(medicamento__isnull=True)
	if 'query' in request.GET and request.GET['query']:
		query = request.GET['query']
		return render_to_response('maps.html',{'query': query, 'farmacias_select': farmacias_select,
								  'farmacias': farmacias, 'medicamentos_select' : medicamentos_select},
								   context_instance = RequestContext(request))
	else:
		return render_to_response('maps.html', {'error': True, 'farmacias_select': farmacias_select,
								  'farmacias': farmacias, 'medicamentos_select': medicamentos_select}, context_instance = RequestContext(request))

def resultados(request):
	#farmacias = Farmacias.objects.filter('local_nombre' = 'FARMACIAS DR. SIMI')
   	farmacias_select = Farmacias.objects.values('local_nombre').annotate(dcount=Count('local_nombre'))
	medicamentos_select = Farmacias.objects.exclude(medicamento__isnull=True)
	if 'query' in request.GET and request.GET['query']:
		query = request.GET['query']
		return render_to_response('resultados.html',{'query': query, 'farmacias_select': farmacias_select,
								  'medicamentos_select' : medicamentos_select},
								   context_instance = RequestContext(request))
	else:
		return render_to_response('maps.html', {'error': True, 'farmacias_select': farmacias_select,
								  'medicamentos_select': medicamentos_select}, context_instance = RequestContext(request))

def filtrofarmacia(request):
	#farmacias = Farmacias.objects.filter(local_nombre = 'FARMACIAS CRUZ VERDE')
   	farmacias_select = Farmacias.objects.values('local_nombre').annotate(dcount=Count('local_nombre'))
	medicamentos_select = Farmacias.objects.exclude(medicamento__isnull=True)
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		farmacias_filtro = Farmacias.objects.filter(local_nombre = q)
		return render_to_response('filtrofarmacia.html',{'q': q, 'farmacias_select': farmacias_select,
								  'farmacias_filtro': farmacias_filtro, 'medicamentos_select' : medicamentos_select},
								   context_instance = RequestContext(request))
	else:
		return render_to_response('filtrofarmacia.html', {'error': True, 'farmacias_select': farmacias_select,
								  'medicamentos_select': medicamentos_select}, context_instance = RequestContext(request))

def filtromedicamentos(request):
	#farmacias = Farmacias.objects.filter(local_nombre = 'FARMACIAS CRUZ VERDE')
   	farmacias_select = Farmacias.objects.values('local_nombre').annotate(dcount=Count('local_nombre'))
	medicamentos_select = Farmacias.objects.values('medicamento').annotate(dcount=Count('medicamento'))
	if 'medic' in request.GET and request.GET['medic']:
		medic = request.GET['medic']
		medicamentos_filtro = Farmacias.objects.filter(medicamento = medic)
		return render_to_response('filtromedicamentos.html',{'medic': medic, 'farmacias_select': farmacias_select,
								  'medicamentos_filtro': medicamentos_filtro, 'medicamentos_select' : medicamentos_select},
								   context_instance = RequestContext(request))
	else:
		return render_to_response('filtromedicamentos.html', {'error': True, 'farmacias_select': farmacias_select,
								  'medicamentos_select': medicamentos_select}, context_instance = RequestContext(request))
