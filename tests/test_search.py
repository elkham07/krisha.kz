from playwright.sync_api import Page

def test_search(page: Page):
    page.goto('https://astana.hh.kz/')
    page.wait_for_load_state('domcontentloaded')
    
    # 2. БОРЬБА С ОКНАМИ: Если вылезет модалка выбора языка, кликаем "Понятно" или закрываем её
    # Используем мягкий локатор. Если окна нет, тест пойдет дальше через секунду
    try:
        if page.locator('button:has-text("Понятно")').is_visible():
            page.locator('button:has-text("Понятно")').click()
    except:
        pass

    
    search_input = page.locator('[data-qa="search-input"]')
    search_input.click()
    search_input.fill('QA Engineering')
    
    
    page.get_by_role('button', name='Найти').click()
    page.wait_for_load_state('networkidle')
    

    page.locator('text="Фильтры"').click()
    page.get_by_role('combobox', name='Астана').click()
    page.get_by_role('checkbox', name='От 1 года до 3').click()
    page.get_by_role('textbox', name='Уровень дохода', exact=False).fill('300000')