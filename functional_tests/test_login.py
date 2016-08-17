from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_cannot_submit_article_without_logging_in(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_title').send_keys('Title')
        self.browser.find_element_by_id('id_text').send_keys('Text')
        self.browser.find_element_by_id('id_categories_1').click()
        self.browser.find_element_by_id('id_city_1').click()
        self.browser.find_element_by_css_selector('.article-form input.button').click()

        container = self.browser.find_element_by_class_name('allauth-container')

        self.assertIn("Log in", container)

    def test_login_with_email(self):
        # Person goes to Togethere and sees login link
        self.browser.get(self.server_url)
        self.browser.find_element_by_css_selector('#auth a').click()

        # Person logs in with their email address
        self.browser.find_element_by_id('id_login').send_keys('testuser@email.com')
        self.browser.find_element_by_id('id_password').send_keys('1234567')
        self.browser.find_element_by_class_name('primaryAction').click()

        # They can see that they’re logged in
        navbar = self.browser.find_element_by_id('auth')
        self.assertIn('You are signed in', navbar.text)
