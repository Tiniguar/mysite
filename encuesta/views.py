from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
#from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pregunta,Seleccion
# Create your views here.

#def index(request):
#	lastest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('encuesta/index.html')
#	context = {
#			'lastest_question_list' : lastest_question_list,	
#	}
#	return HttpResponse(template.render(context, request))


def index(request):
	lastest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
	context = {'lastest_question_list' : lastest_question_list}
	return render(request,'encuesta/index.html', context, )

def detail(request,pregunta_id):
	try:
		pregunta = Pregunta.objects.get(pk=pregunta_id) 
	except Pregunta.DoesNotExist:
		raise http404("Esta Pregunta no existe")
	return render(request,'encuesta/detalle.html',{'pregunta': pregunta})


#def detail(request,pregunta_id):
#	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
#	return render(request,'encuesta/detalle.html',{'pregunta':pregunta})


def results(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta,pk=pregunta_id)		
	return render(request,'encuesta/results.html',{'pregunta': pregunta})

def vote(request, pregunta_id):
		pregunta = get_object_or_404(Pregunta,pk=pregunta_id)
		try:
			pregunta_seleccion = pregunta.seleccion_set.get(pk=request.POST['seleccion'])
		except (KeyError,Seleccion.DoesNotExist ):
			return render(request,'encuesta/detalle.html',{'pregunta': pregunta, 'error_message': "You didn't select a seleccion" })
		else:
			pregunta_seleccion.voto += 1
			pregunta_seleccion.save()
			return HttpResponseRedirect(reverse('encuesta:results', args=(pregunta_id,)))

class graficoView(View):
 	"""docstring for ClassName"""
 	def get(self,request, *args, **kwargs):
 		return render(request,'encuesta/chart.html',{})


def get_data(request,*args,**kwargs):
	data={
		"sales":100,
		"customers":10,
	}
	return JsonResponse(data)


class chartPregunta(APIView):
	"""docstring for chartData"""
	def get(self,request,format=None):

		pregunta = list(Pregunta.objects.all())
		list_selection =[]
		list_pregunta = []
		x=0
		for pre in pregunta:
			list_pregunta.append( pre.pregunta_Nombre)
			list_selection.append( Seleccion.objects.filter(pregunta=pre.id).count()           )
			#list_selection += to_int(Seleccion.objects.filter(pregunta=pre.id).count())
		
		
		data={
			"labels":list_pregunta,
			"default":list_selection,		
		}
		return Response(data)


class chartSeleccion(APIView):
	"""docstring for chartData"""
	def get(self,request,format=None):

		pregunta = list(Seleccion.objects.all())
		list_selection =[]
		list_pregunta = []
		x=0
		for pre in pregunta:
			list_pregunta.append( pre.seleccion_Nombre)
			list_selection.append( pre.voto)
			#list_selection += to_int(Seleccion.objects.filter(pregunta=pre.id).count())
		
		
		data={
			"labels":list_pregunta,
			"default":list_selection,		
		}
		return Response(data)