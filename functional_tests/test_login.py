from .base import FunctionalTest

class LoginTest(FunctionalTest):

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
