from django import template
from django.conf import settings
import os
import locale

register = template.Library()


@register.filter(name='format_currency')
def format_currency(value):
    """
    Filtro inteligente que formatea un número como moneda sin redondear.
    - Muestra los decimales exactos que se ingresaron.
    - Usa '.' para miles y ',' para decimales.
    - Agrega el símbolo '$'.
    """
    try:
        # Si el valor está vacío o es None, no muestra nada.
        if not value:
            return ""

        # Limpiamos el valor que viene del formulario si ya viene formateado
        value_str = str(value).replace('.', '').replace(',', '.')

        # Separamos la parte entera de la decimal
        if '.' in value_str:
            integer_part_str, decimal_part_str = value_str.split('.', 1)
        else:
            integer_part_str, decimal_part_str = value_str, None

        # Convertimos la parte entera a un número para poder formatearla
        integer_part = int(integer_part_str)

        # Configuramos el formato para Argentina
        try:
            locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_ALL, '') # Fallback al locale del sistema

        # Formateamos solo la parte entera con los puntos de miles
        formatted_integer_part = locale.format_string('%d', integer_part, grouping=True)

        # Reconstruimos el número final
        if decimal_part_str is not None:
            # Si había decimales, los volvemos a unir con una coma
            final_number_str = f"{formatted_integer_part},{decimal_part_str}"
        else:
            # Si no había decimales, usamos solo la parte entera
            final_number_str = formatted_integer_part

        return f"$ {final_number_str}"

    except (ValueError, TypeError):
        # Si el valor no es un número válido, lo devolvemos como está.
        return value



@register.filter(name='get_image_path')
def get_image_path(filename):
    """
    Convierte un nombre de archivo de firma en una ruta de sistema de archivos
    completa que el generador de PDF pueda leer.
    """
    if not filename:
        return ""

    # Se ajusta la ruta para que coincida con tu estructura de carpetas.
    image_path = os.path.join(
        settings.BASE_DIR,
        'reports',
        'static',
        'signatures',
        filename
    )
    return image_path