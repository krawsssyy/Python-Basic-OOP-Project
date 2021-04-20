from Domain.Card import Card


class CardService:
    '''
    Represents the service for films
    '''

    def __init__(self, repo, validator):
        self.__card_repo = repo
        self.__card_validator = validator

    def add_card(self, card_id, surname, name, cnp, dateOfBirth, dateOfSignup, points):
        '''
        Adds a card to the list
        :param card_id: - int - the card's id
        :param surname: - str - the surname of the owner of the card
        :param name: - str - the name of the owner of the card
        :param cnp: - int - the owner's numerical code
        :param dateOfBirth: - str - the owner's date of birth
        :param dateOfSignup: - str - the date of the creation of the card
        :param points: - int - the points on the card
        :return:
        '''
        card = Card(card_id, surname, name, cnp, dateOfBirth, dateOfSignup, points)
        self.__card_validator.validate(card)
        self.__card_repo.create(card)

    def read_card(self, card_id=None):
        '''
        Reads a card from the list or all of the cards
        :param card_id: optional, - int - the card id
        :return: a card matching the card id or the list of cards
        '''
        if card_id is None:
            return self.__card_repo.read()
        else:
            return self.__card_repo(card_id)

    def modify_card(self, card):
        '''
        Modifies a card
        :param card: - Card object to be modified
        :return:
        '''
        self.__card_validator.validate(card)
        self.__card_repo.update(card)

    def delete_card(self, card_id):
        '''
        Deletes a given card from the list
        :param card_id: - int - the card's id
        :return:
        '''
        self.__card_repo.delete(card_id)

    def findCard(self, string):
        '''
        Finds a card given a string to be searched
        :param string: - string - the string that is to be contained in the matched cards
        :return: a list of all of the matches
        '''
        cards = self.__card_repo.read()
        return list(filter(lambda card: string in card, cards))
