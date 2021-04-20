from Domain.Film import Film
import random
import string


class FilmService:
    '''
    Represents the service for films
    '''

    def __init__(self, repo, validator, resRepo):
        self.__film_repo = repo
        self.__film_validator = validator
        self.__res_repo = resRepo

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
            return self.__film_repo.read(film_id)

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
        resList = list(self.__res_repo.read())
        resList = resList[:]
        for res in resList:
            if res.film == film_id:
                self.__res_repo.delete(res.id)
        self.__film_repo.delete(film_id)


    def findFilm(self, string):
        '''
        Finds a film given a string to be searched
        :param string: - string - the string that is to be contained in the matched films
        :return: a list of all of the matches
        '''
        films = self.__film_repo.read()
        newList = []
        for film in films:
            if string in str(film.id) or string in str(film.title) or string in str(film.year) or \
                    string in str(film.price) or string in str(film.played):
                newList.append(film)
        return newList

    def populate(self, num):
        '''
        Function to populate the films
        :param num: - int - the amount of films to be added
        :return:
        '''
        readList = self.read_film()
        readList = sorted(readList, key=lambda film: film.id)
        startID = readList[-1].id + 1
        letters = string.ascii_letters
        for index in range(num):
            year = random.randint(1900, 2019)
            played = random.choice(['Da', 'Nu', 'nu', 'da', 'DA', 'NU'])
            price = random.randint(0, 2000)
            title = ''.join(random.choice(letters) for i in range(10))
            self.add_film(startID, title, year, price, played)
            startID += 1

    def binSearch(self, array, left, right, element):
        '''
        Performs a binary search
        :param array: - list - the sorted array
        :param left: - int - the left margin
        :param right: - int - the right margin
        :param element: - int - the element to be searched
        :return: The position of the element in the list if it is in it or -1 otherwise
        '''
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == element:
                return mid
            elif array[mid] < element:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def getIDsList(self):
        '''
        Creates a sorted list of IDs
        :return: a sorted list of IDs
        '''
        list = self.__film_repo.read()
        newList = []
        for film in list:
            newList.append(film.id)
        newList = sorted(newList)
        return newList





