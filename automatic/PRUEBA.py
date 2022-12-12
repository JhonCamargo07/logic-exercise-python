import time

from playwright.sync_api import Playwright, sync_playwright, expect
import random

email = ['sofiacolmenares@gmail.com', 'franchescobulevar@gmail.com', 'martinezsofia@hotmail.com', 'sofiacolmenares@hotmail.com', 'franchescobulevar@hotmail.com', 'martinezsofia@gmail.com']
asunto = ['Prueba automatica con libreria', 'Test python, excelent', 'Message random from random']
message = ['Mucho gusto, mi nombre es... y quiero contratarte. Comunicate al 3100000000, ES URGENTE', 'Que pagina para estar tan bien hecha, felicidades', 'Muy bonita su pagina, felicidades. Att: anonymous, somos legion', 'La pagiona es muy buena, que gran idea hermano']


def send_form(page):
    page.get_by_label("Para *").click()

    page.get_by_label("Para *").fill("jhoncamargo07a@gmail.com")

    page.get_by_label("Para *").press("Tab")

    page.get_by_label("Asunto *").fill(random.choice(asunto))

    page.get_by_label("Asunto *").press("Tab")

    page.locator("textarea[name=\"input-mensaje\"]").fill(random.choice(message))

    page.get_by_role("button", name="Envíar").click()
    page.wait_for_url("http://localhost:8080/JavaMail/Mail")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("http://localhost:8080/JavaMail/")

    return [page, browser, context]


def close_page(context, browser):
    context.close()
    browser.close()


with sync_playwright() as playwright:
    start = time.time()
    page, browser, context = run(playwright)
    for num in range(10):
        send_form(page)
        print(num)
    close_page(context, browser)
    end = time.time()
    print(f'Se demora: {end - start}')
