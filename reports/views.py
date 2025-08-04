from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from .models import ReporteTragamonedas
from .forms import ReporteForm
from xhtml2pdf import pisa

# ================================================================
# CORRECCIÓN EN LA FUNCIÓN 'crear_reporte'
# ================================================================
# reports/views.py

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            # Paso 1: Crea el objeto en memoria, pero NO lo guardes en la BD todavía
            reporte = form.save(commit=False)
            
            # Paso 2: Asigna manualmente el valor al campo que falta
            reporte.establecimiento = "NUEVO CASINO ALBERDI"
            
            # Paso 3: Ahora sí, guarda el objeto completo en la BD
            reporte.save()
            
            messages.success(request, '¡Reporte guardado con éxito!')
            return redirect('lista_reportes')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = ReporteForm()
    return render(request, 'reports/formulario_reporte.html', {'form': form})

# --- Las otras vistas (lista_reportes, editar_reporte, etc.) se mantienen igual ---

def lista_reportes(request):
    reportes = ReporteTragamonedas.objects.all().order_by('-fecha_inicio')
    return render(request, 'reports/lista_reportes.html', {'reportes': reportes})

def editar_reporte(request, pk):
    reporte = get_object_or_404(ReporteTragamonedas, pk=pk)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Reporte N° {reporte.numero_informe} actualizado correctamente!')
            return redirect('lista_reportes')
        else:
            print("Errores en el formulario de edición:", form.errors)
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'reports/formulario_reporte.html', {'form': form, 'editando': True})

def exportar_pdf(request, pk):
    reporte = get_object_or_404(ReporteTragamonedas, pk=pk)
    template_path = 'reports/reporte_pdf.html'
    context = {'reporte': reporte}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_{reporte.numero_informe}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('Hubo un error al generar el PDF.')
    return response