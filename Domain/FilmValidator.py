EPSILON = 0.000000001

class FilmValidator:
    '''
    Represents a validator for a film
    '''
    @staticmethod
    def representsInt(value):
        '''
        Tests if a value can be safely converted to an integer
        :param value: - int - to be tested
        :return: True or False whether the initial condition is satisfied
        '''
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def representsFloat(value):
        '''
        Tests if a value can be safely converted to a float
        :param value: - float - to be tested
        :return: True or False whether the initial condition is satisfied
        '''
        try:
            float(value)
            return True
        except ValueError:
            return False

    def validate(self, film):
        # Validates a film object
        if not self.representsInt(film.id):
            raise ValueError("IDul trebuie sa fie un numar intreg")
        if film.id <= 0:
            raise ValueError("IDul trebuie sa fie strict pozitiv")
        if not self.representsInt(film.year):
            raise ValueError("Anul filmului nu este un numar intreg")
        if film.year < 1900:
            raise ValueError("Anul filmului nu poate fi mai mic decat 1900")
        if not self.representsFloat(film.price):
            raise ValueError("Pretul filmului trebuie sa fie un numar real")
        if film.price <= 0 + EPSILON:
            raise ValueError("Pretul filmului nu poate fi negativ sau 0")
        if film.played not in ["Da", "Nu","da", "nu", "DA", "NU"]:
            raise ValueError("Filmul poate fi doar in program sau nu")
