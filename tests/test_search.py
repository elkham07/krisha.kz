from playwright.sync_api import Page 

def test_search(page: Page):
    page.goto('https://astana.hh.kz/')
    page.get_by_role('textbox', name='QA Engineering')
    page.get_by_role('button', name='Найти').click()
    