import os

import pytest
from playwright.sync_api import sync_playwright

from config.config_reader import load_env_config
from pages.home_page import HomePage
from config.config_reader import load_config


class App:
    def __init__(self, page):
        self.home_page = HomePage(page)


def is_ci():
    return os.getenv("CI") == "true"


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
        headless_mode = True if is_ci() else config['browser_setup']['headless']
        browser = p.chromium.launch(
            headless=headless_mode
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()