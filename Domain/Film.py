class Film:
    '''
    Represents a movie
    '''
    def __init__(self, film_id, title,  year, price, played):
        '''
        Creates a new film object
        :param title: - str - the title of the film
        :param film_id: - int - the id of the film
        :param year: - int - the year of the film's release
        :param price: - float - the price for a ticket to this film
        :param played: - boolean - True/False <=> Yes/No
        '''
        self.__id = film_id
        self.__title = title
        self.__year = year
        self.__price = price
        self.__played = played

    def __str__(self):
        # This method is used to print films with a stable format
        return "'ID' : {}, 'Title' : {}, 'Year' : {}, 'price' : {}, 'in schedule' : {}".\
            format(self.__id, self.__title, self.__year, self.__price, self.__played)

    def __eq__(self, other):
        '''
        Checks if two given objects are films, and afterwards if they are equal
        :param other: - the other given object for comparision
        :return: False - if the two objects have different types, and True/False if they are equal or not
        '''
        if type(self) != type(other):
            return False
        return self.__id == other.__id and self.__year == other.__year and self.__price == other.__price and \
            self.__played == other.__played and self.__title == other.__title

    def __ne__(self, other):
        '''
        Checks if two films are different or not
        :param other: - the other object
        :return: True/False whether self != other
        '''
        return not self == other

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def played(self):
        return self.__played

    @played.setter
    def played(self, value):
        self.__played = value


def test_film():
    pass
