from Domain.CardValidator import CardValidator
from Domain.FilmValidator import FilmValidator
from Domain.ReservationValidator import ReservationValidator
from Repository.CardRepository import CardRepository
from Repository.FilmRepository import FilmRepository
from Repository.ReservationRepository import ReservationRepository
from Service.FilmService import FilmService
from Service.CardService import CardService
from Service.ReservationService import ReservationService
from UI.Console import Console


def main():
    film_repo = FilmRepository("filme.txt")
    card_repo = CardRepository("carduri.txt")
    res_repo = ReservationRepository("rezervari.txt")
    film_validator = FilmValidator()
    card_validator = CardValidator()
    res_validator = ReservationValidator()
    film_service = FilmService(film_repo, film_validator, res_repo)
    card_service = CardService(card_repo, card_validator, res_repo)
    res_service = ReservationService(res_repo, res_validator, film_repo, card_repo)
    ui = Console(film_service, card_service, res_service)
    ui.run()


main()



