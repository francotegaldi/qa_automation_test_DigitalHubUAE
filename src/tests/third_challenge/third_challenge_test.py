from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.board_page import BoardPage
from base.selenium_driver import SeleniumDriver
from api.trello_cards import TrelloCards
from api.trello_lists import TrelloLists
from api.trello_boards import TrelloBoards
from base.trello_driver import TrelloDriver
import pytest
import json

@pytest.mark.usefixtures('first_challenge_setup')
class TestThirdChallenge:

    @pytest.fixture(autouse=True)
    def class_setup(self, first_challenge_setup):
        self.seleniumDriver = SeleniumDriver(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.boardPage = BoardPage(self.driver)

        with open("/src/utils/data.json") as jsonfile:
            self.data = json.load(jsonfile)

        self.trelloCards = TrelloCards(self.data['auth']['api_key'], self.data['auth']['token'])
        self.trelloLists = TrelloLists(self.data['auth']['api_key'], self.data['auth']['token'])
        self.trelloBoards = TrelloBoards(self.data['auth']['api_key'], self.data['auth']['token'])
        self.trelloDriver = TrelloDriver(self.data['auth']['api_key'], self.data['auth']['token'])

        boardId = self.trelloBoards.create_new_board(self.data['third_challenge']['board_name'])['id']
        challenge_list = self.trelloLists.create_list(self.data['third_challenge']['list_name'], boardId)


    @pytest.mark.run(order=3)
    def test_third_challenge(self):
        self.homePage.click_login_button()
        self.loginPage.send_custom_credentials(self.data['third_challenge']['credentials']['email'], self.data['third_challenge']['credentials']['password'])
        self.loginPage.click_login_button()
        self.dashboardPage.click_first_board()
        self.boardPage.click_first_add_card_button()
        self.boardPage.send_card_name(self.data['third_challenge']['card_name'])
        self.boardPage.verify_existence_of_card(self.data['third_challenge']['card_name'])