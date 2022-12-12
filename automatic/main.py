import random
import time

from playwright.sync_api import Playwright, sync_playwright, expect

name = ['Jane Jane', 'John Alex', 'Clark Lfvgf', 'Lexa Contrikru']
last_name = ['Doe', 'Null', 'Undefined']
email = ['janedoe@gmail.com', 'johndoe@gmail.com', 'lastname@hotmail.com']
asunto = ['Prueba automatica con libreria', 'Test python, excelent', 'Message random from random']
message = ['This is a test python with library', 'Esto es una prueba automatizada', 'Mensaje aleatorio con random']


def send_form(page):

    page.get_by_label("Nombre *").click()

    page.get_by_label("Nombre *").fill(random.choice(name) + " " + random.choice(last_name))

    page.get_by_label("Nombre *").press("Tab")

    page.get_by_label("Correo electrónico *").fill(random.choice(email))

    page.get_by_label("Correo electrónico *").press("Tab")

    page.get_by_label("Asunto *").fill(random.choice(asunto))

    page.get_by_label("Mensaje *").fill(random.choice(message))

    page.get_by_role("button", name="Enviar").click()

    # page.locator("#icono_subir i").click()


def close_page(context, browser):
    # ---------------------
    context.close()
    browser.close()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://jhoncamargo.herokuapp.com/")

    page.get_by_role("link", name="About me").click()
    page.wait_for_url("https://jhoncamargo.herokuapp.com/")

    page.get_by_role("link", name="Habilidades").click()
    page.wait_for_url("https://jhoncamargo.herokuapp.com/")

    page.locator("nav:has-text(\"Sobre míHabilidadesContacto\")").get_by_role("link", name="Contacto").click()
    page.wait_for_url("https://jhoncamargo.herokuapp.com/")

    return [page, browser, context]


with sync_playwright() as playwright:
    start = time.time()
    page, browser, context = run(playwright)
    for num in range(1):
        send_form(page)
        print(num)
    time.sleep(123)
    close_page(context, browser)
    end = time.time()
    print(f'Se demora: {end-start}')