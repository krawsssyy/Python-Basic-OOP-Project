from Domain.Reservation import Reservation

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

    def read_res(self, res_id=None):
        '''
        Reads a reservation or a list of reservations
        :param res_id: optional, - int - the reservation's id
        :return: a reservation matching the given id or a list of all reservations
        '''
        if res_id is None:
            return self.__res_repo.read()
        else:
            return self.__res_repo(res_id)

    def modify_film(self, res):
        '''
        Modifies a reservation
        :param res: - Reservation object to be modified
        :return:
        '''
        self.__res_validator.validate(res)
        self.__res_repo.update(res)

    def delete_film(self, res_id):
        '''
        Deletes a given reservation from the list
        :param res_id: - int - the reservation's id
        :return:
        '''
        self.__res_repo.delete(res_id)



