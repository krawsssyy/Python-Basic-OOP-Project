import datetime
EPSILON = 0.000000001


class CardValidator:
    '''
    Represents a validator for a card
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

    def validate(self, card):
        # Validates a card object
        if not self.representsInt(card.id):
            raise ValueError("IDul trebuie sa fie un numar intreg")
        if card.id <= 0:
            raise ValueError("IDul trebuie sa fie strict pozitiv")
        if not self.representsInt(card.cnp):
            raise ValueError("CNPul trebuie sa fie un numar intreg")
        if len(str(card.cnp)) != 13:
            raise ValueError("CNPul trebuie sa aiba 13 cifre")
        if self.representsInt(self.getDay(card.date)) and self.representsInt(self.getMonth(card.date)) and \
                self.representsInt(self.getYear(card.date)):
            if int(self.getDay(card.date)) < 1 or int(self.getMonth(card.date)) < 1 or int(self.getYear(card.date)) < 1:
                raise ValueError("Data a nasterii invalida")
            if int(self.getDay(card.date)) > 31 or int(self.getMonth(card.date)) > 12 or \
                    int(self.getYear(card.date)) > datetime.datetime.now().year:
                raise ValueError("Data a nasterii invalida")
        else:
            raise ValueError("Data a nasterii invalida")
        if self.representsInt(self.getDay(card.signup)) and self.representsInt(self.getMonth(card.signup)) and \
                self.representsInt(self.getYear(card.signup)):
            if int(self.getDay(card.signup)) < 1 or int(self.getMonth(card.signup)) < 1 or\
                    int(self.getYear(card.signup)) < 1:
                raise ValueError("Data a inregistrariii invalida")
            if int(self.getDay(card.signup)) > 31 or int(self.getMonth(card.signup)) > 12 or \
                    int(self.getYear(card.signup)) > datetime.datetime.now().year:
                raise ValueError("Data a inregistrariii invalida")
        else:
            raise ValueError("Data a inregistrariii invalida")
        if not int(self.getYear(card.date)) <= int(self.getYear(card.signup)) + 14:
            raise ValueError("Nu va puteti inregistra pana la varsta de 14 ani")
        if not self.representsInt(card.points):
            raise ValueError("Punctele acumulate trebuie sa fie un numar intreg")
        if card.points < 0:
            raise ValueError("Punctele acumulate trebuie sa fie pozitive")

