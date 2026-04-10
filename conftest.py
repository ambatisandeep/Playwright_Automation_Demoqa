import os

import pytest
from playwright.sync_api import sync_playwright

from config.config_reader import load_env_config
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from config.config_reader import load_config


class App:
    def __init__(self,env_config, page, browser):
        self.home_page = HomePage(env_config,page, browser)
        self.elements_page = ElementsPage(env_config, page, browser)


def is_ci():
    return os.getenv("CI") == "true"


@pytest.fixture
def app(env_config, page, browser):
    return App(env_config, page, browser)


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def env_config():
    return load_env_config()


@pytest.fixture
def browser(config):
    with sync_playwright() as p:
        headless_mode = True if is_ci() else config['browser_setup']['headless']
        browser = p.chromium.launch(
            headless=headless_mode,
            args = ["--start-maximized"]
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()
    yield page
    context.close()
