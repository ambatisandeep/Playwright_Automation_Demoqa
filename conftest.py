import pytest
from playwright.sync_api import sync_playwright
from config.config_reader import load_config

@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config["headless"])
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()