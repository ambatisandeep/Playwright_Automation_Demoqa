import pytest
from playwright.sync_api import sync_playwright

from config.config_reader import load_env_config
from pages.home_page import HomePage
from config.config_reader import load_config

class App:
    def __init__(self, page):
        self.home_page = HomePage(page)

@pytest.fixture
def app(page):
    return App(page)

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def env_config():
    return load_env_config()

@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config['browser_setup']['headless'], args=[config['browser_setup']['maximize']])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()