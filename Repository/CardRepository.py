from Domain.Card import Card
import json


class CardRepository:
    '''
    Repository for cards
    '''
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        # This function is used to load the films from the file
        try:
            with open(self.__filename, 'r') as f_read:
                savedCards = json.load(f_read)
                self.__storage.clear()
                for savedCard in savedCards:
                    card = Card(*savedCard)
                    self.__storage[card.id] = card
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        # This function is used to save the films to the file
        newList = []
        for card in self.__storage.values():
            card_rep = [card.id, card.surname, card.name, card.cnp, card.date, card.signup, card.points]
            newList.append(card_rep)
        with open(self.__filename, 'w') as f_write:
            json.dump(newList, f_write)

    def create(self, card):
        '''
        Adds a new card.
        :param card: the given card
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        if card.id in self.__storage:
            raise DuplicateIDError('The card id already exists')
        for cards in self.__storage.values():
            if card.cnp == cards.cnp:
                raise DuplicateCNPError("The card's cnp already exists")
        self.__storage[card.id] = card
        self.__save_to_file()

    def read(self, card_id=None):
        '''
        Gets a card by id or all the cards
        :param card_id: optional, the card id
        :return: the list of cards or the card with the given id
        '''
        self.__load_from_file()
        if card_id is None:
            return self.__storage.values()
        if card_id in self.__storage:
            return self.__storage[card_id]
        return None

    def update(self, card):
        '''
        Updates a card.
        :param card: the card to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        if card.id not in self.__storage:
            raise NoIDError('There is no card with that id')
        self.__storage[card.id] = card
        self.__save_to_file()

    def delete(self, card_id):
        '''
        Deletes a card.
        :param card_id: the card id to delete.
        :return: -
        :raises KeyError: if no card with card_id
        '''
        self.__load_from_file()
        if card_id not in self.__storage:
            raise NoIDError('There is no card with that id')
        del self.__storage[card_id]
        self.__save_to_file()

    def clear(self):
        '''
        Clears the storage
        :return:
        '''
        self.__storage = {}


class DuplicateIDError(Exception):
    pass


class NoIDError(Exception):
    pass


class DuplicateCNPError(Exception):
    pass

def test_cardRepo():
    pass
