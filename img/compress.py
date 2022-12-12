from PIL import Image
import os

# ruta = os.path.dirname(input('Ruta de la carpeta: '))
ruta = input('Ruta de la carpeta: ')

cont = 1

for nombre in os.listdir(ruta):
    name, extension = os.path.splitext(ruta + nombre)
    if extension in ['.png', '.jpeg', '.jpg']:
        print(os.path.join(ruta + nombre))
        img = Image.open(os.path.join(ruta + nombre))
        img_r = img.convert('RGB')
        img_r.save(f'img_{cont}.jpg', quality=70)
        cont += 1