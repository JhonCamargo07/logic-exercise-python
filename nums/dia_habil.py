"""
Un programa que ingresando una fecha, me muestre cuando se se cumplen 15 dias habililes a partir del dia proporcionado
sin tener en cuenta los festivos
"""
from datetime import datetime
from datetime import timedelta


def get_dia_habil(fecha):
    print('Fecha actual', fecha.date())
    fecha += timedelta(days=21)
    curren_day = fecha.strftime('%A')
    if curren_day == 'Sunday':
        fecha -= timedelta(days=2)
    elif curren_day == 'Saturday':
        fecha -= timedelta(days=1)
    return fecha.date()


print('Fecha proxima', get_dia_habil(datetime.now() - timedelta(days=0)))
