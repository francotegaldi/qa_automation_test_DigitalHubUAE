from base.trello_driver import TrelloDriver
from assertpy import assert_that

class TrelloCards(TrelloDriver):

    def __init__(self, trelloKey, trelloToken):
        super().__init__(trelloKey, trelloToken)
        self.trelloKey = trelloKey
        self.trelloToken = trelloToken


    def create_new_card(self, listId, cardName):
        r = self.post_create_card(listId, cardName)
        return r

    def get_cards_ids(self, boardId):
        r = self.get_cards_from_board(boardId)
        _ids_list = []
        for card in r:
            _ids_list.append(card['id'])
        return _ids_list

    def verify_created_card(self, boardId, cardId):
        r = self.get_cards_ids(boardId)
        assert_that(r).contains(cardId)
