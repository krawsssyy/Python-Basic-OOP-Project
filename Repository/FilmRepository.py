from Domain.Film import Film
import json


class FilmRepository:
    '''
    Repository for films
    '''
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        # This function is used to load the films from the file
        try:
            with open(self.__filename, 'r') as f_read:
                savedFilms = json.load(f_read)
                self.__storage.clear()
                for savedFilm in savedFilms:
                    film = Film(*savedFilm)
                    self.__storage[film.id] = film
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        # This function is used to save the films to the file
        newList = []
        for film in self.__storage.values():
            film_rep = [film.id, film.title, film.year, film.price, film.played]
            newList.append(film_rep)
        with open(self.__filename, 'w') as f_write:
            json.dump(newList, f_write)

    def create(self, film):
        '''
        Adds a new film.
        :param film: the given film
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        if film.id in self.__storage:
            raise KeyError('The film id already exists')
        self.__storage[film.id] = film
        self.__save_to_file()

    def read(self, film_id=None):
        '''
        Gets a film by id or all the films
        :param film_id: optional, the film id
        :return: the list of films or the film with the given id
        '''
        self.__load_from_file()
        if film_id is None:
            return self.__storage.values()
        if film_id in self.__storage:
            return self.__storage[film_id]
        return None

    def update(self, film):
        '''
        Updates a film.
        :param film: the film to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        if film.id not in self.__storage:
            raise KeyError('There is no film with that id')
        self.__storage[film.id] = film
        self.__save_to_file()

    def delete(self, film_id):
        '''
        Deletes a film.
        :param film_id: the film id to delete.
        :return: -
        :raises KeyError: if no film with film_id
        '''
        self.__load_from_file()
        if film_id not in self.__storage:
            raise KeyError('There is no film with that id')
        del self.__storage[film_id]
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


def test_filmRepo():
    pass
