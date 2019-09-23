from api.trello_cards import TrelloCards
from api.trello_lists import TrelloLists
from base.trello_driver import TrelloDriver
import pytest

@pytest.mark.usefixtures('second_challenge_setup')
class TestSecondChallenge:

    @pytest.fixture(autouse=True)
    def class_setup(self, second_challenge_setup):
        self.trelloCards = TrelloCards(self.data['auth']['api_key'], self.data['auth']['token'])
        self.trelloLists = TrelloLists(self.data['auth']['api_key'], self.data['auth']['token'])
        self.trelloDriver = TrelloDriver(self.data['auth']['api_key'], self.data['auth']['token'])

    @pytest.mark.run(order=2)
    def test_second_challenge(self):
        _first_list = self.trelloLists.get_lists_from_board(self.data['second_challenge']['board'])[0]
        _new_card = self.trelloCards.create_new_card(_first_list['id'],self.data['second_challenge']['card_name'])
        self.trelloCards.verify_created_card(self.data['second_challenge']['board'], _new_card['id'])
