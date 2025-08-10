from django.db import models

class ReporteTragamonedas(models.Model):
    # --- DATOS GENERALES ---
    numero_informe = models.IntegerField(unique=True, verbose_name="Número de Informe")
    fecha_inicio = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    marca_juego = models.CharField(max_length=100)
    numero_maquina = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    establecimiento = models.CharField(max_length=100, default="NUEVO CASINO ALBERDI")

    # --- CONTADORES ELECTRÓNICOS (ORDEN CORRECTO) ---
    creditos_jugados_inicio = models.TextField(default='0,00', verbose_name="Créditos Jugados (Inicio)")
    creditos_jugados_cierre = models.TextField(default='0,00', verbose_name="Créditos Jugados (Cierre)")
    creditos_pagados_inicio = models.TextField(default='0,00', verbose_name="Créditos Pagados (Inicio)")
    creditos_pagados_cierre = models.TextField(default='0,00', verbose_name="Créditos Pagados (Cierre)")
    voucher_in_inicio = models.TextField(default='0,00', verbose_name="Voucher In (Inicio)")
    voucher_in_cierre = models.TextField(default='0,00', verbose_name="Voucher In (Cierre)")
    voucher_out_inicio = models.TextField(default='0,00', verbose_name="Voucher Out (Inicio)")
    voucher_out_cierre = models.TextField(default='0,00', verbose_name="Voucher Out (Cierre)")
    jackpot_inicio = models.TextField(default='0,00', verbose_name="Jackpot (Inicio)")
    jackpot_cierre = models.TextField(default='0,00', verbose_name="Jackpot (Cierre)")
    creditos_cancelados_inicio = models.TextField(default='0,00', verbose_name="Créditos Cancelados (Inicio)")
    creditos_cancelados_cierre = models.TextField(default='0,00', verbose_name="Créditos Cancelados (Cierre)")
    creditos_cancelados_totales_inicio = models.TextField(default='0,00', verbose_name="Créditos Cancelados Totales (Inicio)")
    creditos_cancelados_totales_cierre = models.TextField(default='0,00', verbose_name="Créditos Cancelados Totales (Cierre)")
    att_paid_total_won_inicio = models.TextField(default='0,00', verbose_name="ATT PAID TOTAL WON (Inicio)")
    att_paid_total_won_cierre = models.TextField(default='0,00', verbose_name="ATT PAID TOTAL WON (Cierre)")
    juegos_inicio = models.TextField(default='0', verbose_name="Juegos (Inicio)")
    juegos_cierre = models.TextField(default='0', verbose_name="Juegos (Cierre)")
    valor_de_credito_inicio = models.TextField(default='0,00', verbose_name="Valor de Crédito (Inicio)")
    valor_de_credito_cierre = models.TextField(default='0,00', verbose_name="Valor de Crédito (Cierre)")
    drop_inicio = models.TextField(default='0,00', verbose_name="Drop (Inicio)")
    drop_cierre = models.TextField(default='0,00', verbose_name="Drop (Cierre)")
    billetes_inicio = models.TextField(default='0,00', verbose_name="Billetes (Inicio)")
    billetes_cierre = models.TextField(default='0,00', verbose_name="Billetes (Cierre)")
    porcentaje_real_inicio = models.TextField(default='0,00', verbose_name="% Real (Inicio)")
    porcentaje_real_cierre = models.TextField(default='0,00', verbose_name="% Real (Cierre)")
    valor_transmision_inicio = models.TextField(default='0,00', verbose_name="Valor de Transmisión (Inicio)")
    valor_transmision_cierre = models.TextField(default='0,00', verbose_name="Valor de Transmisión (Cierre)")
    # --- OBSERVACIONES ---
    observaciones = models.TextField(blank=True, null=True)


    firma_tecnico = models.CharField(max_length=100, blank=True, null=True, verbose_name="Firma del Técnico")
    firma_jefe_slot = models.CharField(max_length=100, blank=True, null=True, verbose_name="Firma del Jefe de Slot")
    firma_encargado_sala = models.CharField(max_length=100, blank=True, null=True, verbose_name="Firma del Encargado de Sala")
    firma_cajero = models.CharField(max_length=100, blank=True, null=True, verbose_name="Firma del Cajero")

    def __str__(self):
        return f"Reporte {self.numero_maquina} - {self.fecha_inicio.strftime('%Y-%m-%d')}"