from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://krisha.kz/")
    page.get_by_role("link", name="Аренда", exact=True).click()
    page.goto("https://krisha.kz/arenda/")
    page.get_by_role("link", name="Недвижимость в Астане").click()
    page.get_by_role("link", name="Квартиры").nth(1).click()
    page.get_by_role("button").nth(3).click()
    with page.expect_popup() as page1_info:
        page.locator("#id-1012604143").get_by_role("link", name="3-комнатная квартира · 57 м² · 2/7 этаж", exact=True).click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Скрыть подсказку").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
