import re
from playwright.sync_api import Page, expect , BrowserContext

def test_search(page: Page):
    page.goto('https://krisha.kz/', wait_until='commit')
    page.wait_for_timeout(1000)

    page.get_by_role('combobox').nth(2).select_option('2')
    page.get_by_role("textbox", name="До").click()
    page.get_by_role("textbox", name="До").fill("20000000")

    
    page.get_by_role("button", name="Найти").click()
    page.wait_for_timeout(1000)

    page.mouse.wheel(0, 500)
    page.locator('text="Избранное"').first.click()
    page.wait_for_timeout(1000)
    


def test_appartment2(page: Page):
    page.goto('https://krisha.kz/', wait_until='domcontentloaded')
    page.get_by_role('link', name="Избранное").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link").nth(5).click()
    expect(page.get_by_text('Горячие предложения недвижимости в Казахстане')).to_be_visible
    page.wait_for_timeout(1000)




def test_new_developments(page: Page, context: BrowserContext):
    page.goto('https://krisha.kz/', wait_until='domcontentloaded')
    page.get_by_role('link', name="Новостройки").click()
    page.get_by_role("button", name="Скрыть подсказку").click()
    expect(page.get_by_text('Новостройки в Казахстане')).to_be_visible

    with context.expect_page() as new_tab_event:
        page.get_by_role('link', name="Есть видео Isma").click()

        new_tab = new_tab_event.value
        new_tab.wait_for_load_state()


    page.get_by_role("link").nth(5).click()


def test_sort(page: Page):
    page.goto('https://krisha.kz/', wait_until='domcontentloaded')
    page.get_by_role('button', name="Найти").click()
    page.get_by_role('link', name="Новые").click()
    page.wait_for_timeout(500)
    page.get_by_role('link', name="Дешевые").click()
    page.wait_for_timeout(500)
    page.get_by_role('link', name="Дорогие").click()


def test_switching(page: Page):
    page.goto('https://krisha.kz/', wait_until='domcontentloaded')
    page.get_by_role('button', name="Найти").click()
    page.goto("https://krisha.kz/")
    page.get_by_role("button", name="Найти").click()
    page.get_by_role("link", name=" На карте").click()

        
    


