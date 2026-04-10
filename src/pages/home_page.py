from playwright.sync_api import Page
from urllib.parse import urljoin
from config.config_reader import load_env_config
from config.config_reader import load_config


class HomePage:

    def __init__(self,env_config, page: Page, browser):
        self.env_config = env_config
        self.page = page
        self.browser = browser
        self.base_config = load_config()
        self.env_config = load_env_config()
        self.search_input = page.locator('input[name="q"]')
        self.search_button = page.locator('input[type="submit"]')
        self.category_card_text = page.locator(".category-cards h5")
        self.category_card = page.locator(".category-cards a")

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

    def get_category_cards_details_text(self):
        self.navigate()
        self.category_card_text.first.wait_for(state="visible")
        return self.category_card_text

    def get_category_cards_links(self):
        self.navigate()
        self.category_card.first.wait_for(state="visible")
        return self.category_card


    def get_category_card_page(self, category_ele_text):
        category_cards_elements = self.get_category_cards_links()
        category_ele_card = category_cards_elements.filter(has_text=category_ele_text)
        href = category_ele_card.get_attribute("href")
        new_context = self.browser.new_context()
        category_ele_page = new_context.new_page()
        category_ele_page.goto(urljoin(self.env_config["base_url"], href))
        return category_ele_page
