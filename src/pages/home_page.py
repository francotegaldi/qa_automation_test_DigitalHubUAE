from base.selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_button = '.btn-link' #css

    def click_login_button(self):
        self.clickElement(self._login_button, 'css')