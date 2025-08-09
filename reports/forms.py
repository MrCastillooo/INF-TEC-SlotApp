from django import forms
from .models import ReporteTragamonedas

class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteTragamonedas
        fields = '__all__'
        exclude = ['establecimiento']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_cierre': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),

            'firma_tecnico': forms.HiddenInput(),
            'firma_jefe_slot': forms.HiddenInput(),
            'firma_encargado_sala': forms.HiddenInput(),
            'firma_cajero': forms.HiddenInput(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lista de campos que usan el formato de JavaScript
        self.formatted_fields = [
            'creditos_jugados_inicio', 'creditos_jugados_cierre', 'creditos_pagados_inicio',
            'creditos_pagados_cierre', 'voucher_in_inicio', 'voucher_in_cierre',
            'voucher_out_inicio', 'voucher_out_cierre', 'jackpot_inicio', 'jackpot_cierre',
            'creditos_cancelados_inicio', 'creditos_cancelados_cierre',
            'creditos_cancelados_totales_inicio', 'creditos_cancelados_totales_cierre',
            'att_paid_total_won_inicio', 'att_paid_total_won_cierre', 'juegos_inicio',
            'juegos_cierre', 'valor_de_credito_inicio', 'valor_de_credito_cierre',
            'drop_inicio', 'drop_cierre', 'billetes_inicio', 'billetes_cierre',
            'porcentaje_real_inicio', 'porcentaje_real_cierre', 'valor_transmision_inicio',
            'valor_transmision_cierre'
        ]
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        """
        Este método se ejecuta automáticamente durante la validación del formulario.
        Lo usamos para "limpiar" los datos antes de guardarlos.
        """
        cleaned_data = super().clean()
        
        for field_name in self.formatted_fields:
            if field_name in cleaned_data:
                value = cleaned_data.get(field_name)
                if isinstance(value, str):
                    # 1. Quitamos los puntos de miles
                    value_cleaned = value.replace('.', '')
                    # 2. Reemplazamos la coma decimal por un punto
                    value_cleaned = value_cleaned.replace(',', '.')
                    cleaned_data[field_name] = value_cleaned
                    
        return cleaned_data