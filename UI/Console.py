class Console:
    '''
    Represents a console
    '''

    def __init__(self, filmService, cardService, resService):
        self.__film_service = filmService
        self.__card_service = cardService
        self.__res_service = resService

    @staticmethod
    def __menu():
        # Prints the menu
        print("1.Adauga/afiseaza/modifica/sterge filme")
        print("2.Adauga/afiseaza/modifica/sterge carduri")
        print("3.Adauga/afiseaza/modifica/sterge rezervari")
        print("4.Cauta film")
        print("5.Cauta client")
        print("6.Afiseaza toate rezervarile dintr-un interval de ore")
        print("7.Afiseaza filmele ordonate descrescator dupa numarul de rezervari")
        print("8.Afiseaza cardurile ordonate descrescator dupa numarul de puncte")
        print("9.Sterge toate rezervarile dintr-un interval de zile")
        print("10.Incrementeaza cu o valoare punctele cardurilor a caror "
              "detinator are data de nastere intr-un interval dat")
        print("x.Exit")

    @staticmethod
    def __crud_menu():
        # Prints the menu for CRUD operations
        print("a.Adaugati")
        print("b.Afisati lista intreaga")
        print("c.Modificati")
        print("d.Stergeti")

    def run(self):
        # The console itself
        while True:
            self.__menu()
            op = input("Optiune : ")
            if op == '1':
                self.__handle_crudFilm()
            elif op == '2':
                self.__handle_crudCard()
            elif op == '3':
                self.__handle_crudRes()
            elif op == '4':
                self.__handle_filmSearch()
            elif op == '5':
                self.__handle_cardSearch()
            elif op == '6':
                pass
            elif op == '7':
                pass
            elif op == '8':
                pass
            elif op == '9':
                pass
            elif op == '10':
                pass
            elif op == 'x':
                break

    def __handle_crudFilm(self):
        # Handler for the CRUD operations for a film
        self.__crud_menu()
        op = input("Optiune : ")
        if op == 'a':
            try:
                film_id = int(input("ID = "))
                title = input("Titul = ")
                year = int(input("Anul aparitiei = "))
                price = float(input("Pret = "))
                played = input("Este in program? = ")
                self.__film_service.add_film(film_id, title, year, price, played)
                print("Film adaugat")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'b':
            print("Introduceti o valoare a id-ului sau introduceti 0 pentru a afisa toata lista")
            try:
                film_id = int(input("ID ="))
                if film_id == 0:
                    listFilms = self.__film_service.read_film()
                    print(*listFilms)
                else:
                    film = self.__film_service.read_film(film_id)
                    print(film)
            except ValueError as ve:
                print(ve)
        elif op == 'c':
            try:
                from Domain.Film import Film
                film_id = int(input("ID = "))
                title = input("Titul = ")
                year = int(input("Anul aparitiei = "))
                price = float(input("Pret = "))
                played = input("Este in program? = ")
                film = Film(film_id, title, year, price, played)
                self.__film_service.modify_film(film)
                print("Film modificat cu succes")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'd':
            print("Introduceti o valoare a id-ului filmului pe care doriti sa-l stergeti")
            try:
                film_id = int(input("ID ="))
                self.__film_service.delete_film(film_id)
                print("Film sters cu succes")
            except ValueError as ve:
                print(ve)
        else:
            print("Optiune invalida")

    def __handle_crudCard(self):
        # Handler for CRUD operations for a card
        self.__crud_menu()
        op = input("Optiune : ")
        if op == 'a':
            try:
                card_id = int(input("ID = "))
                surname = input("Nume = ")
                name = input("Prenume = ")
                cnp = int(input("CNP = "))
                dateBirth = input("Data nasterii = ")
                dateSignup = input("Data inscrierii =")
                points = int(input("Puncte = "))
                self.__card_service.add_card(card_id, surname, name, cnp, dateBirth, dateSignup, points)
                print("Card adaugat cu succes")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'b':
            print("Introduceti o valoare a IDului sau introduceti 0 pentru a afisa toata lista")
            try:
                card_id = int(input("ID ="))
                if card_id == 0:
                    listCards = self.__card_service.read_card()
                    print(*listCards)
                else:
                    card = self.__card_service.card_film(card_id)
                    print(card)
            except ValueError as ve:
                print(ve)
        elif op == 'c':
            try:
                from Domain.Card import Card
                card_id = int(input("ID = "))
                surname = input("Nume = ")
                name = input("Prenume = ")
                cnp = int(input("CNP = "))
                dateBirth = input("Data nasterii = ")
                dateSignup = input("Data inscrierii =")
                points = int(input("Puncte = "))
                card = Card(card_id, surname, name, cnp, dateBirth, dateSignup, points)
                self.__card_service.modify_card(card)
                print("Card modificat cu succes")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'd':
            print("Introduceti o valoare a IDului cardului pe care doriti sa-l stergeti")
            try:
                card_id = int(input("ID ="))
                self.__card_service.delete_card(card_id)
                print("Card sters cu succes")
            except ValueError as ve:
                print(ve)
        else:
            print("Optiune invalida")

    def __handle_crudRes(self):
        # Handler for CRUD operations for a reservation
        self.__crud_menu()
        op = input("Optiune : ")
        if op == 'a':
            try:
                res_id = int(input("ID = "))
                film_id = int(input("IDul filmului = "))
                card_id = int(input("IDul cardului(pentru a se lasa gol,se pune 0) = "))
                date = input("Data = ")
                hour = int(input("Ora = "))
                if card_id != 0:
                    self.__res_service.add_res(res_id, film_id, date, hour, card_id)
                else:
                    self.__res_service.add_res(res_id, film_id, date, hour)
                print("Rezervare adaugata")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'b':
            print("Introduceti o valoare a IDului sau introduceti 0 pentru a afisa toata lista")
            try:
                res_id = int(input("ID ="))
                if res_id == 0:
                    listRess = self.__res_service.read_res()
                    print(*listRess)
                else:
                    res = self.__res_service.read_res(res_id)
                    print(res)
            except ValueError as ve:
                print(ve)
        elif op == 'c':
            try:
                from Domain.Reservation import Reservation
                res_id = int(input("ID = "))
                film_id = int(input("IDul filmului = "))
                card_id = int(input("IDul cardului(pentru a se lasa gol,se pune 0) = "))
                date = input("Data = ")
                hour = int(input("Ora = "))
                if card_id != 0:
                    res = Reservation(res_id, film_id, date, hour, card_id)
                else:
                    res = Reservation(res_id, film_id, date, hour)
                self.__res_service.modify_res(res)
                print("Rezervare modificata cu succes")
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        elif op == 'd':
            print("Introduceti o valoare a IDului rezervarii pe care doriti s-o stergeti")
            try:
                res_id = int(input("ID ="))
                self.__res_service.delete_res(res_id)
                print("Rezervare stersa cu succes")
            except ValueError as ve:
                print(ve)
        else:
            print("Optiune invalida")

    def __handle_filmSearch(self):
        # Handler for a full-text search in films
        string = input("Introduceti un filtru pentru cautarea filmului")
        result = self.__film_service.findFilm(string)
        print(*result)

    def __handle_cardSearch(self):
        # Handler for a full-text search in cards
        string = input("Introduceti un filtru pentru cautarea cardului")
        result = self.__card_service.findCard(string)
        print(*result)



