from playwright.sync_api import Page

from src.config.config_reader import load_env_config
from src.config.config_reader import load_config

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_config = load_config()
        self.env_config = load_env_config()
        self.search_input = page.locator('input[name="q"]')
        self.search_button = page.locator('input[type="submit"]')

    def navigate(self):
        try:
            self.page.goto(self.env_config['base_url'])
        except Exception as e:
            print(e)


    def get_home_page_title(self):
        try:
            return self.page.title()
        except Exception as e:
            print(e)

    def get_category_cards_details(self):
        try:
            return self.page.locator("div[class='category-cards']/a")
        except Exception as e:
            print(e)




