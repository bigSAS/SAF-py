# każda osoba to słowniczek z atrybutami.
# printy są ćwiczeniowe, wiem że działa funkcja

phenomenelik = {
    'name': 'Piotrek',
    'age': 32,
    'email': 'piotr.menel@gmail.com',
    'pet': None
}

monstersasog = {
    'name': 'Tomek',
    'age': 35,
    'email': 'bigsasit@gmail.com',
    'pet': {
        'name': 'Fifi',
        'species': 'Dog'
    }
}

margotzuk = {
    'name': 'Gosia',
    'age': 37,
    'email': 'margotzuk@gmail.com',
    'pet': {
        'name': 'Celestyna',
        'species': 'Cat'
    }
}

ngsasog = {
    'name': 'Ola',
    'age': 28,
    'email': None,
    'pet': None
}


persons = [phenomenelik, monstersasog, margotzuk, ngsasog]

# ze zwierzakami już nie kombinowałem
pets = [
    {
        'name': 'Bobik',
        'spieces': 'Rabbit'
    },
    {
        'name': 'Hektor',
        'spieces': 'Dog'
    },
    {
        'name': 'Denver',
        'spieces': 'Last Dinosaur'
    }
]


# 0 wyświetla osoby w liście persons
def show_persons(persons):
    for i, person in enumerate(persons, 1):
        print(f'{i}. {person}')


# 0bis wyświetla zwierzaki w liście pets
def show_pets(pets):
     for i, pet in enumerate(pets, 1):
        print(f'{i}. {pet}')

        
show_persons(persons)
show_pets(pets)


# 1. Dodaj osobe do listy PERSON
print('___ZADANIE_1___')
print("")

def add_person(person):
    persons.append(person)
    return persons
  

jaszczur = {
    'name': 'Jasiek',
    'age': 34,
    'email': None,
    'pet': {
        'name': 'Demolka',
        'spieces': 'Cat'
    }
}

add_person(jaszczur)
show_persons(persons)
print('-' * 20)
print("")

# 2. Usun osobe z listy PERSONS -> chciałem użyć na początku pop, ale to musiałbym indeks wskazać
print('___ZADANIE_2___')
print("")

def remove_person(person):
    persons.remove(person)
    return persons
    
pheno = {
    'name': 'Piotrek',
    'age': 32,
    'email': 'piotr.menel@gmail.com',
    'pet': None
}

remove_person(phenomenelik) # zadziala
show_persons(persons)

add_person(phenomenelik)
print('kolejny usun')
remove_person(pheno)
show_persons(persons)

# remove person po emailu
def remove_person_by_email(persons, email):
    for person in persons:
        if person['email'] == email:
	
    	
        	persons.remove(person)
    return persons

remove_person_by_email(persons, 'margotzuk@gmail.com')
show_persons(persons)
  # 3. Dodaj zwierzaka do listy PETS
print('___ZADANIE_3___')
print("")

def add_pet(pet):
  pets.append(pet)
  return pets

add_pet({'name': 'Gawron', 'spieces': 'Bird'})
show_pets(pets)
print('-' * 20)
print("")

# 4. Edytuj zwierzaka z listy PETS - DO ROZKMINY
print('___ZADANIE_4___')
print("")


def update_pet(pets_list, pet_name, new_pet):
    for pet in pets_list:
        if pet['name'] == pet_name:
            pets_list.remove(pet)
            pets_list.append(new_pet)
    return pets_list

new_bobik = {
  'name': 'srobik',
  'species': 'ufo'
}

pets = update_pet(pets, 'Bobik', new_bobik)
show_pets(pets)

print('-' * 20)
print("")


# 5. Znajdz osobe w liscie PERSONS (parametry dowolne poza indexem w liscie - zeby bylo kurwa trudniej)
print('___ZADANIE_5___')
print("")

# nie wiem dlaczego nie działa jak dam key 'name', value 'Piotrek'
def search_person(persons, key, value):
    """ zwraca person jesli znajdzie, jesli nie znajdzie rzuca exception """
    found_person = None
    for person in persons:
        if person.get(key) == value:
            found_person = person
    if not found_person:
        raise Exception(f'person not found: k:{key}, v: {value}')
    else:
    	return found_person

show_persons(persons)
print(search_person(persons, 'email', 'bigsasit@gmail.com'))
try:
	print(search_person(persons, 'name', 'notexisting'))
except:
  	print('not found')

    
# 6. Znajdz zwierzaka w liscie PETS (jw)
print('___ZADANIE_6___')
print("")


def search_pet(pets_list: list, key: str, value):
    found_pet = None
    for pet in pets_list:
      if pet.get(key) == value: found_pet = pet
    if not found_pet:
      raise Exception(f'{key} {value} - not found')
    return found_pet

print(search_pet(pets, 'name', 'Denver'))          

print('-' * 20)
print("")

# 7. Przypisz zwierzaka osobie na liscie PERSONS
print('___ZADANIE_7___')
print("")


def add_pet(person_list, pets_list, person_name, pet_name):
    try:
        persona = search_person(person_list, 'name', person_name)
        petini = search_pet(pets_list, 'name', pet_name)
        persona['pet'] = petini
    except Exception as e:
        print(f'error!\n{e}')

add_pet(
    person_list=persons,
    pets_list=pets,
    person_name='Ola',
    pet_name='Denver'
)

rec_person_name = 'heheszki'
rec_pet_name = 'beng'

add_pet(
    person_list=persons,
    pets_list=pets,
    person_name=rec_person_name,
    pet_name=rec_pet_name
)


show_persons(persons)

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
"""
Lista zwierzakow, tu prosciej jest sobie kilka zwierzakow poprostu, beda potrzebne do operacji na PERSONSach :)
kazdy zwierzak ma dwa atrybuty:
    - name - imie
    - species - gatunek (bmozliwe ze mam literowke -> jebac :) )
"""
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

#print('lesgooooo')





