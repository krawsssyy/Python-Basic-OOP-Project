class Reservation:
    '''
    Represents a reservation
    '''
    def __init__(self, res_id, film_id, date, hour, card_id=None):
        '''
        Creates a reservation object
        :param res_id: - int - the id of the given reservation
        :param film_id: - int - the id of the film to be watched
        :param date: - str - the date of the reservation
        :param hour: - int - the hour at which the film is scheduled to start
        :param card_id: - int - the id of the card that belongs to the person making the reservation
                              - can be left None if the user doesn't have a card
        '''
        self.__id = res_id
        self.__film = film_id
        self.__card = card_id
        self.__res_date = date
        self.__hour = hour

    def __str__(self):
        # This function is used to print a card with a stable format
        return "'ID' : {}, 'Film ID' : {}, 'Card ID' : {}, 'Date' : {}, 'Time' : {}".\
            format(self.__id, self.__film, self.__card, self.__res_date, self.__hour)

    def __eq__(self, other):
        '''
        Checks if two given objects are reservations, and afterwards if they are equal
        :param other: - the other given object for comparision
        :return: False - if the two objects have different types, and True/False if they are equal or not
        '''
        if type(self) != type(other):
            return False
        return self.__id == other.__id and self.__film == other.__film and self.__card == other.__card and\
            self.__res_date == other.__res_date and self.__hour == other.__hour

    def __ne__(self, other):
        '''
        Checks if two reservations are different or not
        :param other: - the other object
        :return: True/False whether self != other
        '''
        return not self == other

    @property
    def id(self):
        return self.__id

    @property
    def film(self):
        return self.__film

    @film.setter
    def film(self, value):
        self.__film = value

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def res_date(self):
        return self.__res_date

    @res_date.setter
    def res_date(self, value):
        self.__res_date = value

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        self.__hour = value


def test_res():
    pass
