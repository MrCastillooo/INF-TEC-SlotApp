# reports/templatetags/report_filters.py

from django import template
from django.utils.safestring import mark_safe
import locale

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