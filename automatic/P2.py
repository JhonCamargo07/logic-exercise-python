import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("http://localhost:8080/JavaMail/")

    page.get_by_label("Para *").click()

    page.get_by_label("Para *").fill("jhoncamargo07a@gmail.com")

    page.get_by_label("Para *").press("Tab")

    page.get_by_label("Asunto *").press("CapsLock")

    page.get_by_label("Asunto *").fill("FELIZ NAVIDAD")

    page.get_by_label("Asunto *").press("Tab")

    page.locator("textarea[name=\"input-mensaje\"]").fill(" ")

    page.get_by_role("button", name="Envíar").click()
    page.wait_for_url("http://localhost:8080/JavaMail/Mail")
    # page.goto("http://localhost:8080/JavaMail/Mail")


    time.sleep(20)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
