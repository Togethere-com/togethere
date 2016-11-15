from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MainTest(FunctionalTest):

    def test_sees_a_list_of_links_and_can_click_them(self):
        # Person visits the site
        self.browser.get(self.server_url)

        # Selects a category
        category = self.browser.find_element_by_id("id_categories__name_0")
        category.click()

        # Selects a city
        city = self.browser.find_element_by_id("id_city__name_0")
        city.click()

        # Hits filter button and filtered articles appear
        filter_button = self.browser.find_element_by_css_selector(".filter form")
        filter_button.click()

        # Sees filtered article
        article_title = self.browser.find_element_by_css_selector("#article_id_1 h2")
        self.assertEqual("foo", article_title.text)

        # Can clear filters
        reset_button = self.browser.find_element_by_id("filter-form-reset-button")
        reset_button.click()
        articles = self.browser.find_elements_by_class_name('article-list__item')
        self.assertGreater(len(articles),0)
