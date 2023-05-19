"""
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/
  mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px.
"""
from fractions import Fraction
import requests
from PIL import Image
from io import BytesIO


def get_aspect_ratio(witdh, height):
    return str(Fraction(witdh, height)).replace('/', ':')


def get_size_img(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    ancho, alto = image.size
    print(f"{ancho} * {alto}")
    return ancho, alto


def obtener_aspect_ratio(ancho, alto):
    if ancho == alto:
        return "1:1 (Cuadrado)"
    elif ancho > alto:
        ratio = ancho / alto
        if ratio == 4 / 3:
            return "4:3 (Pantalla estándar)"
        elif ratio == 16 / 9:
            return "16:9 (Pantalla panorámica)"
        elif ratio == 3 / 2:
            return "3:2 (Formato de película)"
        elif ratio == 5 / 4:
            return "5:4 (Formato cuadrado más alto)"
        elif ratio == 2 / 3:
            return "2:3 (Formato de película inverso)"
        else:
            return f"{ancho}:{alto} (Personalizado)"
    else:
        ratio = alto / ancho
        if ratio == 9 / 16:
            return "9:16 (Vertical)"
        else:
            return f"{ancho}:{alto} (Personalizado)"


# url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
url = input('Ingrese la url: \n')
ancho, alto = get_size_img(url)
print(get_aspect_ratio(ancho, alto))
print(obtener_aspect_ratio(ancho, alto))
