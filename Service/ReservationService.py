from Domain.Reservation import Reservation
from copy import deepcopy


class ReservationService:
    '''
    Represents the logic for a reservation
    '''

    def __init__(self, repo, validator, repoFilm, repoCard):
        self.__res_repo = repo
        self.__res_validator = validator
        self.__film_repo = repoFilm
        self.__card_repo = repoCard

    def add_res(self, res_id, film_id, date, hour, card_id=None):
        '''
        Adds a new reservation to the list
        :param res_id: - int - the reservation's id
        :param film_id: - int - the film's id
        :param date: - str - the date of the reservation
        :param hour: - int - the hour of the film
        :param card_id: optional, - int - the card's id
        :return:
        '''
        isValid = self.__film_repo.read(film_id).played
        if isValid in ["Da", "da", "DA"]:
            res = Reservation(res_id, film_id, date, hour, card_id)
            self.__res_validator.validate(res)
            self.__res_repo.create(res)
            if card_id is not None:
                card = self.__card_repo.read(card_id)
                price = self.__film_repo.read(film_id).price
                card.points += int(price/10)
                self.__card_repo.update(card)
                print(card.points)

    def read_res(self, res_id=None):
        '''
        Reads a reservation or a list of reservations
        :param res_id: optional, - int - the reservation's id
        :return: a reservation matching the given id or a list of all reservations
        '''
        if res_id is None:
            return self.__res_repo.read()
        else:
            return self.__res_repo.read(res_id)

    def modify_res(self, res):
        '''
        Modifies a reservation
        :param res: - Reservation object to be modified
        :return:
        '''
        self.__res_validator.validate(res)
        self.__res_repo.update(res)

    def delete_res(self, res_id):
        '''
        Deletes a given reservation from the list
        :param res_id: - int - the reservation's id
        :return:
        '''
        self.__res_repo.delete(res_id)

    def getResByHours(self, beginHour, endHour):
        '''
        Gets reservations that are between a given hour interval
        :param beginHour: - int - beginning hour for the interval
        :param endHour: - int - end hour for the interval
        :return: - list that contains the reservations that are in that hour interval
        '''
        results = self.__res_repo.read()
        newList = []
        for result in results:
            if beginHour <= result.hour <= endHour:
                newList.append(result)
        return newList

    def delResByDates(self, beginDate, endDate):
        '''
        Deletes reservations that are between a given date interval
        :param beginDate: - string - beginning date
        :param endDate: - string - end date
        :return:
        '''
        results = self.__res_repo.read()
        for result in deepcopy(list(results)):
            if int(self.__res_validator.getYear(beginDate)) <= int(self.__res_validator.getYear(result.res_date)) <= \
                    int(self.__res_validator.getYear(endDate)):
                if int(self.__res_validator.getMonth(beginDate)) <= int(self.__res_validator.getMonth(result.res_date))\
                        <= int(self.__res_validator.getMonth(endDate)):
                    if int(self.__res_validator.getDay(beginDate)) <= int(self.__res_validator.getDay(result.res_date))\
                            <= int(self.__res_validator.getDay(endDate)):
                        self.delete_res(result.id)

    def getFilms(self):
        '''
        Gets the amount of reservations per film
        :return: - dictionary containing the film id and the number of reservations it has
        '''
        results = self.__res_repo.read()
        resultDict = {}
        for result in results:
            if result.film_id in resultDict.keys():
                resultDict[result.film_id] += 1
            else:
                resultDict[result.film_id] = 1
        return resultDict

    def validateDate(self, date):
        '''
        Validates a given date
        :param date: - string - the date
        :return: True or False,whether the date is valid or nah
        '''
        if self.__res_validator.representsInt(self.__res_validator.getDay(date)) and \
                self.__res_validator.representsInt(self.__res_validator.getMonth(date)) and\
                self.__res_validator.representsInt(self.__res_validator.getYear(date)):
            if 1899 < int(self.__res_validator.getYear(date)) < 2020:
                if 0 < int(self.__res_validator.getMonth(date)) <= 12:
                    if 1 <= int(self.__res_validator.getDay(date)) < 32:
                        return True
        return False




