import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Pregunta(models.Model):
	"""docstring for Pregunta"""
	pregunta_Nombre = models.CharField (max_length=200)
	pub_date = models.DateTimeField('Date Published')

	def __str__(self):
		return self.pregunta_Nombre
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Seleccion(models.Model):
	"""docstring for Seleccion"""
	pregunta = models.ForeignKey (Pregunta,on_delete=models.CASCADE)
	seleccion_Nombre = models.CharField(max_length=200)
	voto = models.IntegerField(default=0)	

	def __str__(self):
		return self.seleccion_Nombre