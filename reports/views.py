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

# reports/views.py

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():

            ultimo_reporte = ReporteTragamonedas.objects.order_by('-numero_informe').first()

            if ultimo_reporte:
                # ================================================================
                # CORRECCIÓN: Convertimos el número (que es texto) a un entero (int) antes de sumar.
                # ================================================================
                nuevo_numero = int(ultimo_reporte.numero_informe) + 1
            else:
                nuevo_numero = 3500

            reporte = form.save(commit=False)
            reporte.numero_informe = nuevo_numero
            reporte.establecimiento = "NUEVO CASINO ALBERDI"
            reporte.save()

            messages.success(request, f'¡Reporte N° {nuevo_numero} guardado con éxito!')
            return redirect('lista_reportes')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = ReporteForm()
    return render(request, 'reports/formulario_reporte.html', {'form': form})
# --- Las otras vistas (lista_reportes, editar_reporte, etc.) se mantienen igual ---

def lista_reportes(request):
    # CORRECCIÓN: Ordenamos por '-id'. El guion (-) asegura que el ID más alto (el más nuevo) aparezca primero.
    reportes = ReporteTragamonedas.objects.all().order_by('-id')
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


def borrar_reporte(request, pk):
    # Solo permitir borrado a través de POST para seguridad
    if request.method == 'POST':
        # Buscar el reporte por su ID
        reporte = get_object_or_404(ReporteTragamonedas, pk=pk)

        # Guardar el número para el mensaje antes de borrar
        numero_informe = reporte.numero_informe

        # Borrar el objeto de la base de datos
        reporte.delete()

        # Crear mensaje de éxito
        messages.success(request, f'El Reporte N° {numero_informe} ha sido borrado exitosamente.')

    # Redirigir siempre a la lista de reportes
    return redirect('lista_reportes')
