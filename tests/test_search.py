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

