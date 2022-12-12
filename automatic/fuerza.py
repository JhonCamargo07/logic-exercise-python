from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://einstructor.datasena.com/login")

    page.get_by_placeholder("Número Identificación").click()

    page.get_by_placeholder("Número Identificación").fill("1010101010")

    page.get_by_placeholder("Contraseña").click()

    page.get_by_placeholder("Contraseña").fill("1010101010")

    page.get_by_role("button", name="Ingresar").click()
    page.wait_for_url("https://einstructor.datasena.com/login")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
