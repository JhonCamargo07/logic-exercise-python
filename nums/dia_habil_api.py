import requests
from datetime import datetime, timedelta


def get_festivos_COL(year):
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/CO"
    response = requests.get(url)
    data = response.json()
    festivos = []
    print(data)
    if response.status_code == 200:
        for holiday in data:
            festivos.append(holiday["date"])
    print(festivos)
    return festivos


def calcular_siguientes_dias_habiles(fecha, cantidad):
    festivos = get_festivos_COL(fecha.year)
    dias_habiles = []
    dia_actual = fecha
    while len(dias_habiles) < cantidad:
        dia_actual += timedelta(days=1)
        if dia_actual.weekday() < 5 and str(dia_actual.date()) not in festivos:
            dias_habiles.append(dia_actual.date())
    return dias_habiles


fecha_inicial = datetime(2023, 6, 1)  # Fecha inicial proporcionada
cantidad_dias = 15  # Cantidad de días hábiles a calcular

dias_habiles = calcular_siguientes_dias_habiles(fecha_inicial, cantidad_dias)
print(f'Ultimo día habil: {dias_habiles[-1]}')
