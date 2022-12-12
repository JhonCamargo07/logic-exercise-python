from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("http://127.0.0.1:5173/")

    page.get_by_role("button", name="Iniciar sesión").click()

    page.get_by_role("textbox", name="Correo").click()

    page.get_by_role("textbox", name="Correo").fill("jhonalex@gmail.com")

    page.get_by_role("textbox", name="Contraseña").click()

    page.get_by_role("textbox", name="Contraseña").fill("1234567890")

    page.get_by_role("button", name="Ingresar").click()

    page.get_by_text("Las credenciales son incorrectas").click()

    try:
        print(page.get_by_text("Usuario correcto").click())
        print(page.get_by_text("Las credenciales son incorrectas").click())
    except Exception as e:
        print(e)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
