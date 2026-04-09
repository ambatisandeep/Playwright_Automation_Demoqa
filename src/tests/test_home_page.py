from conftest import app

class TestHomePage:

    def test_home_page_title(self,app):
        app.home_page.navigate()
        actual_title = app.home_page.get_home_page_title()
        assert actual_title == "demosite"

    def test_home_page_category_titles(self,app):
       expected_category_titles = ["Elements","Forms","Alerts, Frame & Windows",
                                   "Widgets","Interactions","Book Store Application"]

       category_cards_elements = app.home_page.get_category_cards_details().all()
       actual_category_titles = [element.inner_text() for element in category_cards_elements]
       assert actual_category_titles == expected_category_titles

