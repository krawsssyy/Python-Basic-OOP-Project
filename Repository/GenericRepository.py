import pickle
from Repository.FilmRepository import FilmRepository


class GenericRepository(FilmRepository):

    def __init__(self, filename):
        super(GenericRepository, self).__init__()
        self.__filename = filename

    def __load_from_file(self):
        # This function is used to load the entities from the file
        try:
            with open(self.__filename, 'rb') as f_read:
                saved_entities = pickle.load(f_read)
                super(GenericRepository, self).clear()
                for entity in saved_entities:
                    super(GenericRepository, self).create(entity)
        except FileNotFoundError:
            super(GenericRepository, self).clear()
        except Exception:
            pass

    def __save_to_file(self):
        # This function is used to save the entities to the file
        to_save = []
        for entity in super(GenericRepository, self).read():
            to_save.append(entity)
        with open(self.__filename, 'wb') as f_write:
            pickle.dump(to_save, f_write)

    def create(self, entity):
        '''
        Adds a new entity.
        :param entity: the given entity
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        super(GenericRepository, self).create(entity)
        self.__save_to_file()

    def read(self, entity_id=None):
        '''
        Gets a vote by id or all the votes
        :param entity_id: optional, the vote id
        :return: the list of entities or the entity with the given id
        '''
        self.__load_from_file()
        return super(GenericRepository, self).read()

    def update(self, entity):
        '''
        Updates vote.
        :param entity: the vote to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        super(GenericRepository, self).update(entity)
        self.__save_to_file()

    def delete(self, entity_id):
        '''
        Deletes a entity.
        :param entity_id: the vote id to delete.
        :return: -
        :raises KeyError: if no entity with entity_id
        '''
        self.__load_from_file()
        super(GenericRepository, self).delete(entity_id)
        self.__save_to_file()

    def clear(self):
        '''
        Clears the storage
        :return:
        '''
        super(GenericRepository, self).clear()