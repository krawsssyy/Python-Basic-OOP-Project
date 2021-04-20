class Card:
    '''
    Represents a client card
    '''
    def __init__(self, card_id, surname, name, cnp, dateOfBirth, dateOfSignup, points):
        '''
        Creates a new card object
        :param card_id: - int - the id of the card
        :param surname: - str - The last name of the person that has the card
        :param cnp: - int - the person's personal numerical code
        :param name: - str - The first name of the person that has the card
        :param dateOfBirth: - str - The date of the birth in the format dd.mm.yyyy for the person that has the card
        :param dateOfSignup: - str - The date in which the person signed up for a client card in the format dd.mm.yyyy
        :param points: - int - the amount of points they have on their card
        '''
        self.__id = card_id
        self.__surname = surname
        self.__name = name
        self.__cnp = cnp
        self.__date = dateOfBirth
        self.__signup = dateOfSignup
        self.__points = points

    def __str__(self):
        # This function is used to print a card with a stable format
        return "'ID' : {}, 'Last Name' : {}, 'First Name' : {}, 'CNP' : {}, 'Date of Birth' : {}, " \
               "'Date of Sign-up' : {}, 'Points' :{}".\
            format(self.__id, self.__surname, self.__name, self.__cnp, self.__date, self.__signup, self.__points)

    def __eq__(self, other):
        '''
        Checks if two given objects are cards, and afterwards if they are equal
        :param other: - the other given object for comparision
        :return: False - if the two objects have different types, and True/False if they are equal or not
        '''
        if type(self) != type(other):
            return False
        return self.__id == other.__id and self.__surname == other.__surname and self.__name == other.__name and\
            self.__cnp == other.__cnp and self.__date == other.__date and self.__signup == other.__signup and \
            self.__points == other.__points

    def __ne__(self, other):
        '''
        Checks if two cards are different or not
        :param other: - the other object
        :return: True/False whether self != other
        '''
        return not self == other

    @property
    def id(self):
        return self.__id

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, value):
        self.__cnp = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def signup(self):
        return self.__signup

    @signup.setter
    def signup(self, value):
        self.__signup = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value


def test_card():
    pass
