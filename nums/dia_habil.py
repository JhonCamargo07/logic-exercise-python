"""
Un programa que ingresando una fecha, me muestre cuando se se cumplen 15 dias habililes a partir del dia proporcionado
"""
from datetime import datetime
from datetime import timedelta


def dia(fecha):
    print('Fecha actual', fecha, fecha.strftime('%A'))

    curren_day = fecha.strftime('%A')
    count = 0
    if curren_day == 'Sunday' or curren_day == 'Saturday':
        fecha += timedelta(days=21)
        print('festivo',  fecha.strftime('%A'))
        if fecha.strftime('%A') == 'Sunday':
            fecha += timedelta(days=1)
        elif fecha.strftime('%A') == 'Saturday':
            fecha += timedelta(days=2)
        return fecha
    else:
        return fecha + timedelta(days=21)

    # test = fecha.date()
    # fecha2 = fecha.date()
    # for day in range(count):
    #     test = test + timedelta(days=1)
    #     test2 = test.strftime('%A')
    #     if test2 != 'Sunday' and test2 != 'Saturday':
    #         fecha2 = fecha + timedelta(days=1)
    #
    #     print(fecha2)

    # print(fecha2.date(),  test, test - fecha2.date())
    # return test


# Obtener la fecha actual
# fecha_actual = datetime.now().date()

# Obtener el día de la semana
# dia_semana = datetime.now()
# dia_semana = dia_semana - timedelta(days=1)
# dia_semana = dia_semana.strftime('%A')
# Convertir la fecha y el día a str
# fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')

# print(f"Fecha actual: {fecha_actual_str}")
# print(f"Día de la semana: {dia_semana}")


print('Fecha proxima', dia(datetime.now() - timedelta(days=1)))