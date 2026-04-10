import re

from conftest import app
from playwright.sync_api import expect


class TestElementsPage:

    def test_elements_page_url(self,app):
        category_ele_page = app.elements_page.navigate_to_elements_page(app)
        expect(category_ele_page).to_have_url(re.compile(r".*/elements$"))


