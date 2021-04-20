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
        print("11.Populati filmele")
        print("12.Undo")
        print("13.Redo")
        print("14.Cautati filmele dupa id")
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
                self.__handle_showResByHours()
            elif op == '7':
                self.__handle_order()
            elif op == '8':
                self.__handle_orderCards()
            elif op == '9':
                self.__handle_delResByDates()
            elif op == '10':
                self.__handle_increment()
            elif op == '11':
                self.__handle_populate()
            elif op == '12':
                pass
            elif op == '13':
                pass
            elif op == '14':
                self.__handle_binSearch()
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
            except KeyError as die:
                print(die)
            except ValueError as ve:
                print(ve)
        elif op == 'b':
            print("Introduceti o valoare a id-ului sau introduceti 0 pentru a afisa toata lista")
            try:
                film_id = int(input("ID ="))
                if film_id == 0:
                    listFilms = self.__film_service.read_film()
                    for film in listFilms:
                        print(film)
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
            except KeyError as nie:
                print(nie)
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
            except KeyError as nie:
                print(nie)
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
            except KeyError as die:
                print(die)
            except KeyError as dce:
                print(dce)
            except ValueError as ve:
                print(ve)
        elif op == 'b':
            print("Introduceti o valoare a IDului sau introduceti 0 pentru a afisa toata lista")
            try:
                card_id = int(input("ID ="))
                if card_id == 0:
                    listCards = self.__card_service.read_card()
                    for card in listCards:
                        print(card)
                else:
                    card = self.__card_service.read_card(card_id)
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
            except KeyError as nie:
                print(nie)
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
            except KeyError as nie:
                print(nie)
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
            except KeyError as die:
                print(die)
            except ValueError as ve:
                print(ve)
            except AttributeError:
                print("ID-ul precizat la film sau card nu exista")
            except IndexError as ie:
                print(ie)
        elif op == 'b':
            print("Introduceti o valoare a IDului sau introduceti 0 pentru a afisa toata lista")
            try:
                res_id = int(input("ID ="))
                if res_id == 0:
                    listRess = self.__res_service.read_res()
                    for res in listRess:
                        print(res)
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
            except KeyError as nie:
                print(nie)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif op == 'd':
            print("Introduceti o valoare a IDului rezervarii pe care doriti s-o stergeti")
            try:
                res_id = int(input("ID ="))
                self.__res_service.delete_res(res_id)
                print("Rezervare stersa cu succes")
            except ValueError as ve:
                print(ve)
            except KeyError as nie:
                print(nie)
        else:
            print("Optiune invalida")

    def __handle_filmSearch(self):
        # Handler for a full-text search in films
        string = input("Introduceti un filtru pentru cautarea filmului")
        result = self.__film_service.findFilm(string)
        if result is None:
            print("Nu s-au gasit rezultate")
        else:
            for res in result:
                print(res)

    def __handle_cardSearch(self):
        # Handler for a full-text search in cards
        string = input("Introduceti un filtru pentru cautarea cardului")
        result = self.__card_service.findCard(string)
        if result is None:
            print("Nu s-au gasit rezultate")
        else:
            for res in result:
                print(res)

    def __handle_populate(self):
        # Handler for the populate function for films
        try:
            num = int(input("Introduceti cate filme doriti sa introduceti"))
            self.__film_service.populate(num)
            print("Populare reusita")
            for film in self.__film_service.read_film():
                print(film)
        except ValueError:
            print("Numarul trebuie sa fie un numar intreg")

    def __handle_order(self):
        # Handler for the order function for films
        listFilms = self.__film_service.read_film()
        dictRes = self.__res_service.getFilms()
        result = []
        for film in listFilms:
            if film.id in dictRes.keys():
                result.append([dictRes[film.id], film])
            else:
                result.append([0, film])
        auxList = sorted(result, key=lambda x: x[0], reverse=True)
        for index in range(len(auxList)):
            print("Numar de rezervari: ", auxList[index][0])
            print(auxList[index][1])
            print("")

    def __handle_delResByDates(self):
        # Handler for deleting of the reservation by given dates
        beginDate = input("Dati data de inceput =")
        endDate = input("Dati data de sfarsit =")
        ok = 0
        try:
            if self.__res_service.validateDate(beginDate) and self.__res_service.validateDate(endDate):
                self.__res_service.delResByDates(beginDate, endDate)
                ok = 1
                print("Operatiune reusita")
            if ok == 0:
                print("Introduceti date corecte si reincercati")
        except IndexError:
            print("Introduceti o data valida")

    def __handle_showResByHours(self):
        # Handler for the showing reservations that are between a given time interval
        try:
            beginHour = int(input("Dati ora de inceput = "))
            endHour = int(input("Dati ora de final = "))
            if 0 <= beginHour < 24 and 0 <= endHour < 24 and beginHour < endHour:
                result = self.__res_service.getResByHours(beginHour, endHour)
                for res in result:
                    print(res)
            else:
                print("Introduceti niste ore in intervalul [0,24) iar ora de inceput sa fie mai mica decat cea de final")
        except ValueError:
            print("Introduceti numere intregi")

    def __handle_orderCards(self):
        # Handler for ordering the cards descending by the number of points they have
        listCards = self.__card_service.order_cards()
        for card in listCards:
            print(card)

    def __handle_increment(self):
        # Handler for the incrementation of points for cards
        try:
            value = int(input("Dati o valoare pentru a incrementa punctele : "))
            beginDate = input("Dati data de inceput = ")
            endDate = input("Dati data de sfarsit = ")
            ok = 0
            if value >= 0:
                if self.__res_service.validateDate(beginDate) and self.__res_service.validateDate(endDate):
                    self.__card_service.birthdayInDate(beginDate, endDate, value)
                    print("Operatiune reusita")
                    ok = 1
            else:
                print("Introduceti un numar intreg pozitiv pentru valoarea incrementarii")
            if ok == 0:
                print("Operatiune esuata.Verificati datele si incercati din nou")
        except ValueError:
            print("Introduceti un numar intreg pozitiv pentru valoarea incrementarii")
        except IndexError:
            print("Introduceti o data valida")

    def __handle_binSearch(self):
        list = self.__film_service.getIDsList()
        try:
            toSearch = int(input("Introduceti IDul cardului "))
            val = self.__film_service.binSearch(list, 0, len(list) - 1, toSearch)
            if val != -1:
                print("Elementul este la pozitia" + str(val))
                print(self.__film_service.read_card(toSearch))
            else:
                print("Elementul nu este in lista")
        except ValueError:
            print("Introduceti un numar intreg valid pentru id")
        except Exception:
            pass






