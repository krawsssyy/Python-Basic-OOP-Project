from Domain.Film import Film


class FilmService:
    '''
    Represents the service for films
    '''

    def __init__(self, repo, validator):
        self.__film_repo = repo
        self.__film_validator = validator

    def add_film(self, film_id, title, year, price, played):
        '''
        Validates and creates a new film
        :param film_id: - int - the film's id
        :param title: - str - the film's title
        :param year: - int - the film's year of release
        :param price: - float - the price for a ticket to this film
        :param played: - str - representing a bool value,if it is still played or not
        :return:
        '''
        film = Film(film_id, title, year, price, played)
        self.__film_validator.validate(film)
        self.__film_repo.create(film)

    def read_film(self, film_id=None):
        '''
        Reads a film from the list or all of the films
        :param film_id: optional, - int - the film id
        :return: a film matching the film id or the list of films
        '''
        if film_id is None:
            return self.__film_repo.read()
        else:
            return self.__film_repo(film_id)

    def modify_film(self, film):
        '''
        Modifies a film
        :param film: - Film object to be modified
        :return:
        '''
        self.__film_validator.validate(film)
        self.__film_repo.update(film)

    def delete_film(self, film_id):
        '''
        Deletes a given film from the list
        :param film_id: - int - the film's id
        :return:
        '''
        self.__film_repo.delete(film_id)

    def findFilm(self, string):
        '''
        Finds a film given a string to be searched
        :param string: - string - the string that is to be contained in the matched films
        :return: a list of all of the matches
        '''
        films = self.__film_repo.read()
        return list(filter(lambda film: string in film, films))
