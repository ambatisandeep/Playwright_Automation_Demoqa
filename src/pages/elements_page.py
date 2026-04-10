from playwright.sync_api import Page

from config.config_reader import load_env_config
from config.config_reader import load_config


class ElementsPage:

    def __init__(self,env_config, page: Page, browser):
        self.page = page
        self.env_config = env_config
        self.browser = browser
        self.base_config = load_config()
        self.env_config = load_env_config()
        self.search_input = page.locator('input[name="q"]')
        self.search_button = page.locator('input[type="submit"]')
        self.category_card_text = page.locator(".category-cards h5")

    def navigate_to_elements_page(self, app):
        category_ele_page = app.home_page.get_category_card_page("Elements")
        return category_ele_page
