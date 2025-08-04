from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_reporte, name='crear_reporte'),
    path('reportes/', views.lista_reportes, name='lista_reportes'),
    path('reportes/editar/<int:pk>/', views.editar_reporte, name='editar_reporte'),
    path('reportes/pdf/<int:pk>/', views.exportar_pdf, name='exportar_pdf'),
]