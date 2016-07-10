from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MainTest(FunctionalTest):

    def test_sees_a_list_of_links_and_can_click_them(self):
        # Person visits the site
        self.browser.get(self.server_url)

        # See Django in the title
        self.assertIn("Togethere", self.browser.title)

        # Styles are being loaded
        height_of_logo = self.browser.find_element_by_css_selector("#logo").value_of_css_property('height')
        self.assertEqual(height_of_logo, '48px')
