import datetime


class ReservationValidator:
    '''
    Represents a validator for a reservation
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
    def getDay(date):
        '''
        Gets the day of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the day of that date
        '''
        aux = date.split(".")
        return aux[0]

    @staticmethod
    def getMonth(date):
        '''
        Gets the month of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the month of that date
        '''
        aux = date.split(".")
        return aux[1]

    @staticmethod
    def getYear(date):
        '''
        Gets the year of a given date in the format dd.mm.yyyy
        :param date: - string - the date
        :return: - string - the year of that date
        '''
        aux = date.split(".")
        return aux[2]

    def validate(self, res):
        # Validates a reservation object
        if not self.representsInt(res.id):
            raise ValueError("IDul trebuie sa fie un numar intreg")
        if res.id <= 0:
            raise ValueError("IDul trebuie sa fie un numar strict pozitiv")
        if not self.representsInt(res.film):
            raise ValueError("IDul filmului trebuie sa fie un numar intreg")
        if res.film <= 0:
            raise ValueError("IDul filmului trebuie sa fie un numar strict pozitiv")
        if res.card is not None and not self.representsInt(res.card):
            raise ValueError("IDul cardului de client trebuie sa fie un numar intreg")
        if res.card is not None and res.card <= 0:
            raise ValueError("IDul cardului de client trebuie sa fie un numar strict pozitiv")
        if self.representsInt(self.getDay(res.res_date)) and self.representsInt(self.getMonth(res.res_date)) and \
                self.representsInt(self.getYear(res.res_date)):
            if int(self.getDay(res.res_date)) < 1 or int(self.getMonth(res.res_date)) < 1 or int(self.getYear(res.res_date)) < 1:
                raise ValueError("Data a rezervarii invalida")
            if int(self.getDay(res.res_date)) > 31 or int(self.getMonth(res.res_date)) > 12 or \
                    int(self.getYear(res.res_date)) > datetime.datetime.now().year:
                raise ValueError("Data a rezervarii invalida")
        else:
            raise ValueError("Data a rezervarii invalida")
        if not self.representsInt(res.hour):
            raise ValueError("Ora trebuie sa fie un numar intreg")
        if not 0 <= res.hour < 24:
            raise ValueError("Ora trebuie sa fie in intervalul [0,24)")


