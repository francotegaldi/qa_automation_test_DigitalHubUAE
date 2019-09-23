from base.trello_driver import TrelloDriver

class TrelloLists(TrelloDriver):

    def __init__(self, trelloKey, trelloToken):
        super().__init__(trelloKey, trelloToken)
        self.trelloKey = trelloKey
        self.trelloToken = trelloToken

    def get_lists_from_board(self, boardId):
        return self.get_lists(boardId)

    def create_list(self, listName, boardId):
        return self.post_create_list(listName, boardId)
