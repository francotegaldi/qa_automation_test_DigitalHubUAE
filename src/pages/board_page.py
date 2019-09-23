from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
from assertpy import assert_that

class BoardPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _all_add_new_card_button = "//a[@class='open-card-composer js-open-card-composer']" #xpath, it returns a list with all add card buttons
    _card_name_input = "//textarea[@class='list-card-composer-textarea js-card-title']" #xpath, since there can only be one add card text input at a time, it is valid
    _add_card_button = "//div[@class='list-card-members js-list-card-composer-members']" #xpath, same as above
    _all_card_names_list = "//span[@class='list-card-title js-card-name']" #xpath, returns a list of all card names

    # This method will click on the first add card button it finds, this is used for the first challenge
    def click_first_add_card_button(self):
        self.clickElementFromList(self._all_add_new_card_button, 'xpath', 0)

    def send_card_name(self, cardName):
        self.sendKeys(self._card_name_input, 'xpath', cardName)
        self.sendKeys(self._card_name_input, 'xpath', Keys.RETURN)
        self.sendKeys(self._card_name_input, 'xpath', Keys.ESCAPE)

    # This method will only verify the existence of 'testCard' only, used in the first challenge
    # Since the first challenge did not specify the board or card to be created, I hardcoded its name for the sake of simplicity
    def verify_existence_of_testCard(self):
        _card_names = self.generate_list_of_elements_text(self._all_card_names_list, 'xpath')
        assert_that(_card_names).contains('testCard')

    # Essentially the same as above but with a card name argument
    def verify_existence_of_card(self, cardName):
        _card_names = self.generate_list_of_elements_text(self._all_card_names_list, 'xpath')
        assert_that(_card_names).contains(cardName)