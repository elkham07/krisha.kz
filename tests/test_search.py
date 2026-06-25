from playwright.sync_api import Page

def test_search(page: Page):
    page.goto('https://krisha.kz/')
    page.wait_for_timeout(1000)

    page.get_by_role('combobox').nth(2).select_option('2')
    page.get_by_role("textbox", name="До").click()
    page.get_by_role("textbox", name="До").fill("2 000 0000")
    page.get_by_role("button", name="Найти").click()
    page.wait_for_timeout(1000)