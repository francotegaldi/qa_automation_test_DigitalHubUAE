from base.selenium_driver import SeleniumDriver

class DashboardPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _all_boards = "//a[@class='board-tile']" #xpath, locator for a list of all boards

    # This method will only select the first board, it is used for the first challenge
    def click_first_board(self):
        self.clickElementFromList(self._all_boards, 'xpath', 0)

    # This method will select the board imported from the json file, it is used for the third challenge
    def click_specific_board(self, boardName):
        pass