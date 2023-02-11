import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright, email) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("http://localhost:8080/JavaMail/")

    page.get_by_label("Para *").click()

    page.get_by_label("Para *").fill(email)

    page.get_by_label("Para *").press("Tab")

    page.get_by_label("Asunto *").press("CapsLock")

    page.get_by_label("Asunto *").fill("F")

    page.get_by_label("Asunto *").press("CapsLock")

    page.get_by_label("Asunto *").fill("Feliz navidad 2465897")

    page.get_by_label("Asunto *").press("Tab")

    page.locator("textarea[name=\"input-mensaje\"]").fill(" ")

    page.get_by_role("button", name="Envíar").click()

    page.wait_for_url("http://localhost:8080/JavaMail/Mail")

    time.sleep(3)

    # page.get_by_role("link", name="Inicio").click()
    #
    # page.wait_for_url("http://localhost:8080/JavaMail/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    with open('C:\\Users\\jhona\\Downloads\\correos.txt', 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            print(linea)
            run(playwright, linea)

