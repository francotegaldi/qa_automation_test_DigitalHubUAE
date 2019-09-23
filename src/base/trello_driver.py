import requests

class TrelloDriver():

    def __init__(self, trelloKey, trelloToken):
        self.trelloKey = trelloKey
        self.trelloToken = trelloToken

    def generate_endpoints(self, request, boardId=None, listId=None, cardName=None, boardName=None, listName=None):
        _key_and_token = f'key={self.trelloKey}&token={self.trelloToken}'

        endpoints = {
            'getAllBoards':'https://api.trello.com/1/members/me/boards?',
            'getBoard':f'https://api.trello.com/1/boards/{boardId}&',
            'getLists':f'https://api.trello.com/1/boards/{boardId}/lists?',
            'getCards':f'https://api.trello.com/1/boards/{boardId}/cards?',
            'postCreateCard':f'https://api.trello.com/1/cards?idList={listId}&name={cardName}&pos=bottom&',
            'postCreateBoard':f'https://api.trello.com/1/boards/?name={boardName}&',
            'postCreateList':f'https://api.trello.com/1/lists?name={listName}&idBoard={boardId}&'
        }

        return f'{endpoints[request]}{_key_and_token}'

    def get_all_boards(self):
        r = requests.get(self.generate_endpoints('getAllBoards'))
        return r.json()

    def get_board(self, boardId):
        r = requests.get(self.generate_endpoints('getBoard', boardId=boardId))
        return r.json()

    def get_lists(self, boardId):
        r = requests.get(self.generate_endpoints('getLists', boardId=boardId))
        listsArray = []
        for lists in r.json():
            listsArray.append(lists['id'])
        print(f'Retrieved lists from board id {boardId}:\n{listsArray}')
        return r.json()

    def get_cards_from_board(self, boardId):
        r = requests.get(self.generate_endpoints('getCards', boardId=boardId))
        return r.json()

    def post_create_card(self, listId, cardName):
        r = requests.post(self.generate_endpoints('postCreateCard', listId=listId, cardName=cardName))
        print(f'Created a new card!\n{r.json()}')
        return r.json()

    def post_create_board(self, boardName):
        r = requests.post(self.generate_endpoints('postCreateBoard', boardName=boardName))
        print(f'Created a new board!\n{r.json()}')
        return r.json()

    def post_create_list(self, listName, boardId):
        r = requests.post(self.generate_endpoints('postCreateList', listName=listName, boardId=boardId))
        print(f'Created new List on board with id {boardId}!\n{r.json()}')
        return r.json()