from Domain.Card import Card
import datetime


class CardService:
    '''
    Represents the service for films
    '''

    def __init__(self, repo, validator, resRepo):
        self.__card_repo = repo
        self.__card_validator = validator
        self.__res_repo = resRepo

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
            return self.__card_repo.read(card_id)

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
        resList = list(self.__res_repo.read())
        resList = resList[:]
        for res in resList:
            if res.card == card_id:
                self.__res_repo.delete(res.id)
        self.__card_repo.delete(card_id)

    def findCard(self, string):
        '''
        Finds a card given a string to be searched
        :param string: - string - the string that is to be contained in the matched cards
        :return: a list of all of the matches
        '''
        cards = self.__card_repo.read()
        newList = []
        for card in cards:
            if string in str(card.id) or string in str(card.surname) or string in str(card.name) or \
                    string in str(card.cnp) or string in str(card.date) or string in str(card.signup) or \
                    string in str(card.points):
                newList.append(card)
        return newList

    def order_cards(self):
        '''
        Orders descending the list of cards given their number of points
        :return: - the sorted list
        '''
        cards = self.__card_repo.read()
        result = sorted(cards, key=lambda card: card.points, reverse=True)
        return result

    @staticmethod
    def getDay(date):
        '''
        Gets the day of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the day of that date
        '''
        aux = date.split(".")
        return aux[0]

    @staticmethod
    def getMonth(date):
        '''
        Gets the month of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the month of that date
        '''
        aux = date.split(".")
        return aux[1]

    @staticmethod
    def getYear(date):
        '''
        Gets the year of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the year of that date
        '''
        aux = date.split(".")
        return aux[2]

    def birthdayInDate(self, beginDate, endDate, givenValue):
        '''
        Increments with a given amount of points all the cards that have their birthdays in the given time interval
        :param beginDate: - string - the beginning date
        :param endDate: - string - the end date
        :param givenValue: - int - the value used to increment the points
        :return:
        '''
        cards = self.__card_repo.read()
        start = datetime.datetime.strptime(beginDate, "%d.%m.%Y")
        end = datetime.datetime.strptime(endDate, "%d.%m.%Y")
        for card in cards:
            currDate = datetime.datetime(day=int(self.getDay(card.date)), month=int(self.getMonth(card.date)), year=int(self.getYear(card.date)))
            if start <= currDate <= end:
                card.points += givenValue
                self.__card_repo.update(card)





def test_cardService():
    from Repository.CardRepository import CardRepository
    from Domain.CardValidator import CardValidator
    from Repository.ReservationRepository import ReservationRepository
    from Domain.Card import Card
    card_repo = CardRepository("TestCard.txt")
    card_valid = CardValidator()
    res_repo = ReservationRepository("TestRepoCard.txt")
    serv = CardService(card_repo, card_valid, res_repo)
    card1 = Card(1, "Alex", "Andrei", 1234567890123, "30.08.2000", "14.12.2015", 150)
    card2 = Card(2, "Alexei", "Andreiu", 1234567890124, "31.05.2000", "14.12.2015", 140)
    card3 = Card(3, "Alexa", "Andrea", 1234567890125, "29.12.2000", "14.12.2015", 170)
    serv.add_card(1, "Alex", "Andrei", 1234567890123, "30.08.2000", "14.12.2015", 150)
    serv.add_card(2, "Alexei", "Andreiu", 1234567890124, "31.05.2000", "14.12.2015", 140)
    serv.add_card(3, "Alexa", "Andrea", 1234567890125, "29.12.2000", "14.12.2015", 170)
    assert len(serv.read_card()) == 3
    assert serv.read_card(1) == card1
    assert serv.read_card(2) == card2
    assert serv.read_card(3) == card3
    assert serv.read_card(5) is None
    assert serv.order_cards() == [card3, card1, card2]
    assert serv.findCard("Anamaria") == []
    serv.birthdayInDate("29.08.2000", "01.09.2000", 100)
    assert serv.read_card(1).points == 250
    serv.delete_card(3)
    serv.delete_card(2)
    assert len(serv.read_card()) == 1


if __name__ == "__main__":
    test_cardService()








