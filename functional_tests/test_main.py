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

        # Sees articles
        articles = self.browser.find_elements_by_class_name('article-list__item')
        self.assertGreater(len(articles),0)

        # Can click them to visit the url and a new page/tab actually opens
        firstarticle = articles[0]
        firstlink = firstarticle.find_element_by_tag_name('a').click()
        self.assertGreater(len(self.browser.window_handles), 0)

        # Sees that articles are in a category
        category_name = self.browser.find_element_by_css_selector(".content article footer")
        self.assertGreater(len(category_name.text),15)

        # Sees categories and articles in them
        self.browser.find_element_by_css_selector(".site-header nav a").click()
        categories_list_item = self.browser.find_element_by_css_selector(".content ul li a")
        self.assertEqual(categories_list_item.text, "General information")

        # Sees articles in the category
        categories_list_item.click()
        articles_in_category = self.browser.find_elements_by_class_name('article-list__item')
        self.assertGreater(len(articles_in_category),0)
