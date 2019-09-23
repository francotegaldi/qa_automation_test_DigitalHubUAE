from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.board_page import BoardPage
from base.selenium_driver import SeleniumDriver
import pytest

@pytest.mark.usefixtures('first_challenge_setup')
class TestFirstChallenge:

    @pytest.fixture(autouse=True)
    def class_setup(self, first_challenge_setup):
        self.seleniumDriver = SeleniumDriver(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.boardPage = BoardPage(self.driver)

    @pytest.mark.run(order=1)
    def test_first_challenge(self):
        self.homePage.click_login_button()
        self.loginPage.send_credentials()
        self.loginPage.click_login_button()
        self.dashboardPage.click_first_board()
        self.boardPage.click_first_add_card_button()
        self.boardPage.send_card_name('testCard')
        self.boardPage.verify_existence_of_testCard()