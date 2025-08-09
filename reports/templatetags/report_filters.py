# reports/templatetags/report_filters.py

from django import template
from django.utils.safestring import mark_safe
import locale
from django import template
from django.conf import settings
import os


register = template.Library()

@register.filter(name='format_currency')
def format_currency(value):
    try:
        if isinstance(value, str):
            value = float(value.replace('.', '').replace(',', '.'))
        
        try:
            locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_ALL, '')

        formatted_value = locale.format_string('%.2f', value, grouping=True)
        return mark_safe(f"$ {formatted_value}")
        
    except (ValueError, TypeError):
        return value
    

@register.filter(name='get_image_path')
def get_image_path(filename):
    if not filename:
        return ""
    
    # CORRECCIÓN: Se ajusta la ruta para que coincida con tu estructura de carpetas.
    # Ahora busca dentro de la carpeta 'reports'.
    image_path = os.path.join(
        settings.BASE_DIR, 
        'reports', 
        'static', 
        'signatures', 
        filename
    )
    return image_path