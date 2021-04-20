import datetime


class ReservationValidator:
    '''
    Represents a validator for a reservation
    '''
    @staticmethod
    def representsInt(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def getDay(date):
        aux = date.split(".")
        return aux[0]

    @staticmethod
    def getMonth(date):
        aux = date.split(".")
        return aux[1]

    @staticmethod
    def getYear(date):
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
            if int(self.getDay(res.res_datee)) > 31 or int(self.getMonth(res.res_date)) > 12 or \
                    int(self.getYear(res.res_date)) > datetime.datetime.now().year:
                raise ValueError("Data a rezervarii invalida")
        else:
            raise ValueError("Data a rezervarii invalida")
        if not self.representsInt(res.hour):
            raise ValueError("Ora trebuie sa fie un numar intreg")
        if not 0 <= res.hour < 24:
            raise ValueError("Ora trebuie sa fie in intervalul [0,24)")


