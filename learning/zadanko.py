"""
Zadanko z funkcji - projektowania itd all around :)
! Important !
Zapoznaj sie dokladnie z trescia zadania - jesli czegos nie rozumiesz -> pytaj :)

Zanim zacznies pizgac kody, zaplanuj sobie -> zidentyfikuj problemy i rozpisz ich rozwiazania, ulatwi to omawianie co jest ok, co nie ;)

Zadanko:
Zaprojektuj (przygotuj zestaw funkcji), ktore pozwola na przetwarzanie danych. Nastepnie wywolaj funkcje aby przedstawic dzialanie programu.   
Na potrzeby zadania obiekty nie beda reprezentowane przez klasy tylko slowniki (slowniki juz znasz i w sumie bardziej przypominaja struktury z ferryta -> zamiast cos.atrybut bedziesz uzywac cos['klucz'] aby odczytac atrybut obiektu)
Przyklad:
person = {
    'name': 'jimmy',
    'age': 66
}

jimmy_name = person['name']
jimmy_age = person['age']

No wiec chcialbym abys zaprojektowal sobie nastepujaca logike.
Nizej w kodzie znajduje sie lista ludziow, oraz lista zwierzat -> PERSONS oraz PETS
"""

"""
lista osob, maja atrybuty:
    - name - imie -> str
    - age - wiek -> str
    - email - email -> str jesli ma email None jesli nie ma -> czyli gosc moze lub nie posiadac email
    - pet - zwierz -> dict -> jesli ma slownik reprezentujacy zwierzaka, jesli nie to None
    
Jak widac wyjsciowa lista przechowuje rozne osoby jeden ma email ale nie ma zwierzaka, inny ma zwierzaka ale nie ma emaila, inny nie ma ani maila ani zwierzaka itd ;)
Zrobilem to specjalnie bo pozwoli to wykonac wiecej operacji na tych danych i w jakis tam sposob ma przelozenie na prawdziwe zycie jak cos sie kodzi, nie zawsze otrzymujesz takie dane jak bys chcial, musisz je w jakis sposob przemielic zeby nadawaly sie do twojego programu :) to samo masz w ferrycie tylko w bardziej popierdolony sposob B-) tu jest o wiele latwiej (jak oswoisz sie z programowaniem :))
"""
PERSONS = [
    {
        'name': 'jimmy',
        'age': 33,
        'email': 'jimmy@choo.org',
        'pet': None
    },
    {
        'name': 'billy',
        'age': 35,
        'email': None,
        'pet': {
            'name': 'hellokitty',
            'species': 'cat'
        }
    },
    {
        'name': 'hellen',
        'age': 25,
        'email': 'hell@enah.com',
        'pet': {
            'name': 'snoop',
            'species': 'dog'
        }
    },
    {
        'name': 'sosad',
        'age': 40,
        'email': None,
        'pet': None
    },
]

"""
Lista zwierzakow, tu prosciej jest sobie kilka zwierzakow poprostu, beda potrzebne do operacji na PERSONSach :)
kazdy zwierzak ma dwa atrybuty:
    - name - imie
    - species - gatunek (bmozliwe ze mam literowke -> jebac :) )
"""
PETS = [
    {
        'name': 'angry',
        'species': 'bird'
    },
    {
        'name': 'fjus',
        'species': 'dog'
    },
    {
        'name': 'bunny',
        'species': 'rabbit'
    }
]


"""
OK czyli masz PERSONS i PETS, niby nic takiego, dwie listy ze slownikami, ale ...
. . .
. . .
. . . .
. . . . . :)
Chcialbym abys napisal zestaw funkcji - bede je numerowal i prosilbym abys przy kazdej definicji funkcji dawal w komentarzu jej nr, ew kopiowal opis np.
def zrob_cos():
    ''' 1 - zrob cos tam '''
    return 'bengbeng!'

Ok przygotuj nastepujace funkcje (mozesz je traktowac jako akcje / eventy w ferrycie):
Niech te funkcje nie uzywaja zadnych input() tylko przyjmuja odpowiednie parametry zapewniajace ich poprawne dzialanie :)
    1. Dodaj osobe do listy PERSONS
    2. Usun osobe z listy PERSONS
    3. Dodaj zwierzaka do listy PETS
    4. Edytuj zwierzaka z listy PETS
    5. Znajdz osobe w liscie PERSONS (parametry dowolne poza indexem w liscie - zeby bylo kurwa trudniej)
    6. Znajdz zwierzaka w liscie PETS (jw)
    7. Przypisz zwierzaka osobie na liscie PERSONS
    8. Zabierz zwierzaka osobie na liscie PERSONS

Jak juz bedziesz mial gotowe funkcje, chcialbym abys z ich uzyciem wykonal operacje:
1. Dodal 3 nowe osoby do listy PERSONS
2. Usunal jedna osobe z listy PERSONS
3. Dodal 2 zwierzaki do listy PETS
4. Dla osob które nie mają maili przypisal zwierzaka (dowolnego z listy pets)
5. Znalazl tylko te osoby ktore posiadaja psy :)
6. Dla osob z pkt 5 zmienil nazwy psiakow -> dodal do nich ' - happy :)'

! HINT ! funkcje, ktore wczesniej zdefiniowales powinny (tak mi sie wydaje na oko) umozliwic ci te wszystkie operacje, ale jesli uznasz ze ci czegos brakuje -> oczywiscie smialo mozesz dodac sobie jakas kolejna funkcje ktora ulatwi ci prace z zadaniem.
! HINT 2 ! to wszystko da sie spokojnie malymi klockami zbudowac i wykonac te operacje wywolujac proste funkcje

! HINT 3 ! z uzyciem ww funckji mozesz sobie dowolnie przygotowac te listy, mozesz tez je modyfikowac jesli ci sie podoba, jedyne co to nie zmieniaj ich struktur - nie potrzeba :)


Do dziela :) - na poczatku pewnie wyda ci sie straszne to - ale w rzeczywistosci to jest bardzo proste, i w sumie wiekszosc (jesli nie wszystko) co tu jest to juz robiles w jakis tam sposob :)
"""

print('lesgooooo')
