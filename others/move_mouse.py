import pyautogui as pag
import time

while True:
    time.sleep(10)
    position_ini = pag.position()
    print(f"Posición actual del mouse: x={position_ini[0]}, y={position_ini[1]}")
    time.sleep(60)
    position_fin = pag.position()
    print(f"Posición actual del mouse: x={position_fin[0]}, y={position_fin[1]}")
    if position_ini == position_fin:
        x = position_fin[0] + 2  # Mover 1 píxel a la derecha
        y = position_fin[1] + 1  # Mover 1 píxel hacia abajo
        pag.move(x, y, duration=0.1)
