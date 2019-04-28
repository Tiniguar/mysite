from django.urls import path

from . import views
from .views import graficoView, chartPregunta,chartSeleccion

app_name = 'encuesta'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pregunta_id>/', views.detail, name='detail'),
    path('<int:pregunta_id>/results/', views.results, name='results'),
    path('<int:pregunta_id>/vote/', views.vote, name='vote'),

    path('api/data/', views.get_data, name='api-data'),    	
    path('api/chart/pregunta', chartPregunta.as_view()),
     path('api/chart/seleccion', chartSeleccion.as_view()),
    path('grafico/', graficoView.as_view(), name='grafico'),
]