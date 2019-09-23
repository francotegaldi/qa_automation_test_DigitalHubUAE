from base.trello_driver import TrelloDriver

class TrelloBoards(TrelloDriver):

    def __init__(self, trelloKey, trelloToken):
        super().__init__(trelloKey, trelloToken)
        self.trelloKey = trelloKey
        self.trelloToken = trelloToken

    def create_new_board(self, boardName):
        return self.post_create_board(boardName)