from Domain.Reservation import Reservation
import json


class ReservationRepository:
    '''
    Repository for reservations
    '''
    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        # This function is used to load the reservations from the file
        try:
            with open(self.__filename, 'r') as f_read:
                savedReses = json.load(f_read)
                self.__storage.clear()
                for savedRes in savedReses:
                    res = Reservation(*savedRes)
                    self.__storage[res.id] = res
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        # This function is used to save the reservations to the file
        newList = []
        for res in self.__storage.values():
            res_rep = [res.id, res.film, res.res_date, res.hour,  res.card]
            newList.append(res_rep)
        with open(self.__filename, 'w') as f_write:
            json.dump(newList, f_write)

    def create(self, res):
        '''
        Adds a new reservation.
        :param res: the given reservation
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        if res.id in self.__storage:
            raise KeyError('The reservation id already exists')
        self.__storage[res.id] = res
        self.__save_to_file()

    def read(self, res_id=None):
        '''
        Gets a reservation by id or all the reservations
        :param res_id: optional, the reservation id
        :return: the list of reservations or the reservation with the given id
        '''
        self.__load_from_file()
        if res_id is None:
            return self.__storage.values()
        if res_id in self.__storage:
            return self.__storage[res_id]
        return None

    def update(self, res):
        '''
        Updates a reservation.
        :param res: the reservation to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        if res.id not in self.__storage:
            raise KeyError('There is no reservation with that id')
        self.__storage[res.id] = res
        self.__save_to_file()

    def delete(self, res_id):
        '''
        Deletes a reservation.
        :param res_id: the reservation id to delete.
        :return: -
        :raises KeyError: if no reservation with res_id
        '''
        self.__load_from_file()
        if res_id not in self.__storage:
            raise KeyError('There is no reservation with that id')
        del self.__storage[res_id]
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


def test_resRepo():
    pass