from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://einstructor.datasena.com/login")

    page.get_by_placeholder("Número Identificación").click()

    page.get_by_placeholder("Número Identificación").fill("1014737507")

    page.get_by_placeholder("Contraseña").click()

    page.get_by_placeholder("Contraseña").fill("1014737507")

    page.get_by_role("button", name="Ingresar").click()
    page.wait_for_url("https://einstructor.datasena.com/home")

    page.get_by_role("link", name=" Ejecutar evaluación").click()
    page.wait_for_url("https://einstructor.datasena.com/assessment")

    page.get_by_label("Digite el código de la evaluación").click()

    page.get_by_label("Digite el código de la evaluación").fill("FY9rqS2vxZ")

    page.get_by_role("button", name="Confirmar").click()

    page.locator(".btn").first.click()

    page.locator("#answers1").get_by_text("Siempre").click()

    page.locator("#answers2").get_by_text("Siempre").click()

    page.locator("#answers3").get_by_text("Siempre").click()

    page.locator("#answers4").get_by_text("Siempre").click()

    page.locator("#answers5").get_by_text("Siempre").click()

    page.locator("#answers6").get_by_text("Siempre").click()

    page.locator("#answers7").get_by_text("Siempre").click()

    page.locator("#answers8").get_by_text("Siempre").click()

    page.locator("#answers9").get_by_text("Siempre").click()

    page.locator("#answers10").get_by_text("Siempre").click()

    page.locator("#answers11").get_by_text("Siempre").click()

    page.locator("#answers12").get_by_text("Siempre").click()

    page.get_by_role("button", name="Enviar").click()

    page.get_by_role("button", name="Aceptar").click()

    page.get_by_role("link").nth(1).click()
    page.wait_for_url("https://einstructor.datasena.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
