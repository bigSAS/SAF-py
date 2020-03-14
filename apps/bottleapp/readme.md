# Bottle app :)   
* bottle
* pony
* goodies

## todo back:
* [] user model
* [] auth
* [] jwt   

## todo front:
* vue POC
  * [x] router
  * [x] tpl components
  * [] store
  * [] different component includes based on view? (smaller vue apps?)


# 4 Piter
# Wypozyczalnia samochodow.
Napisz zestaw klas z metodami + program test (zadekladrowanie obiektow i wywolanie na nich ich metod) ktory potwierdzi ich dzialanie. Calosc powinna odwzorowywac jakas logiczna calosc i zawierac raisowanie exceptionow jesli jakies zalozenia logiczne itd nie sa spelnione.   
Kometarze mile widziane i printy co sie dzieje w danym momencie.   
## Wymagania:
* glowna klasa powinna byc wypozyczalnia (np CarLoan)   
  wypozyczalnia powinna dawac mozliwosc:
    * zarejestrowania klienta (Client)
    * wypozyczenie przez klienta samochodu (Loan)
      informacje na temat wypozyczonych samochodow powinny byc przechowywane   
      czyli: 
        * kto wypozyczyl
        * od kiedy
        * do kiedy
        * jaki samochod (Car)
        * jaki jest koszt wypozyczenia
        * czy oplata pobrana od razu czy bedzie placone przy oddawaniu
    * powinna zawierac magazyn samochodowy (np CarStorage)
      magazyn powinien dac mozliwosc :
        * dodania / usuniecia samochodu
        * samochody powinny byc podzielone na kategorie, modele (CarCategory)
        * powinny miec przypisane koszty dziennego wypozyczenia
    * mozna dodac wlasne ficzery wedle uznania np:
      * rabaty dla klientow VIP
      * mechanizm oplacania w ratach
