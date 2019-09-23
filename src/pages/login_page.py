from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_input = 'user' #id
    _password_input = 'password' #id
    _login_button = 'login' #id
    _email = 'qacodechallenge@gmail.com'
    _password = 'p4ssw0rd'

    # This one has the credentials hardcoded in itself, it is used for the first challenge
    def send_credentials(self):
        self.sendKeys(self._email_input, 'id', self._email)
        self.sendKeys(self._password_input, 'id', self._password)
        print(f'Logged in with credentials\nid: {self._email}\npassword: {self._password}')

    def click_login_button(self):
        self.clickElement(self._login_button, 'id')

    # This one will use credentials provided, used in the third challenge
    def send_custom_credentials(self, id, psw):
        self.sendKeys(self._email_input, 'id', id)
        self.sendKeys(self._password_input, 'id', psw)
        print(f'Logged in with credentials\nid: {id}\npassword: {psw}')