import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsap.com/send?phone=+573142577567')
sleep(10)

with open('message.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
    pyautogui.press('enter')