#Zad. 1
print('ZADANIE 1')
print(" ")
"""
zadeklaruj zmienne przedstawiajace typy danych jakie znasz, wykonaj na nich jakies operacje charaktnie baerystyczne dla danego typu danych
"""
# integer
print('INTEGER')
int1 = 1
int2 = 3
sintr = "1"  
# @sas: to nie jest int tylko str prawdopodobnie chciales pokazac rzutowanie nieswiadomie
type(sintr) # @sas: -> str
int_from_str = int(sintr)  # @sas: funkcja int() rzutuje (zmienia typ) na int (jesli ten str to poprawna liczba, jak dasz int('yolo') -> to bedziesz mial error :) )
type(int_from_str) # @sas: -> int

int3 = int1 + int2
print(int3)
int4 = int1 * int2
print(int4)
int5 = int2 // (int1 + int(sintr))

print(int5)
#można od razu pizdnąć wynik
print(int1 * int2 * int(sintr))
#i tak dalej z matematycznymi równaniami...
# @sas: no powiedzmy ze ok
# @sas: ogolnie int czyli liczby calkowite
age = 20  # @sas zmienna age przechowujaca int o wartosci 20
type(age)  # @sas -> inttakt

# string
print('STRING')
sas = 'monsterSASog'
menel = 'phenomenelik'

# można od razu printnąć
print(f'{sas} uczy {menel} kodzić w pythonie')

sentence = '{} uczy {} kodzić w pythonie'.format(sas, menel)
print(sentence)

strint = str(int5)
print(strint)

sasmenel = sas + " " + menel
print(sasmenel)
# @sas stringi ogarniasz calkiem legit, nic dziwnego wiekszosc danych w ferryt to stringi ;) hehe
# @sas tak odemnie to funkcja str() analogicznie jak funkcja int() rzutuje typ danych czyli
# jesli chcesz z liczby zrobic stringa to str(liczba) np str(1) -> "1" stringi sa zawsze w qouetach (cudzyslowach) moga byc podwojne lub pojedyncze :)


# @sas
# z takich prymitywnych typow danych to pominales
# float czyli liczby zmiennoprzecinkowe np transfer_cost = 2.01 
# bool czyli prawda falsz czyli True / False np is_cool = True


#listy
print('LIST')
fortnite = []


piotrek = 'phenomenelik'
tomek = 'monsterSASog'
ola = 'ngSASog'
pawcio = 'niepamietamnickupawcia'

fortnite.append(piotrek)
fortnite.append(tomek)
fortnite.append(ola)
fortnite.append(pawcio)
print(fortnite)

#ponieważ Pawcio z nami nie gra
fortnite.pop(-1)
print(fortnite)
fortnite.append(pawcio)
print(fortnite.index(pawcio))
fortnite.remove(pawcio)
print(fortnite)
fortnite.insert(3, pawcio)
print(fortnite)

# @sas listy ok , tak odemnie [] to to samo co wywolanie funckji list()
# mozna np od razu zadeklarowac liste np
pets = ['dog', 'cat']
# to to samo co
petz = list()
petz.append('dog')
petz.append('cat')
type(pets) # -> list
type(petz) # -> list

#tuple
print('TUPLE')
fortnite_tuple = tuple(fortnite)
print(fortnite_tuple)
print(fortnite_tuple.index('phenomenelik'))
#dużo z tymi tuplami się nie da
# @sas tuple, ok -> jedyne co trzeba wiedziec na temat tupli to ze nawiasy zwykle zamiast kwadratowych, i ze ELEMENTOW TUPLI nie mozna zmieniac (mutowac) fachowo mowi ze ze tuplea to niemutowalna lista :)
# dodatkowo fajny bajer mozna "rozpakowywac" zawartosc tupli do kilku zmiennych na raz np:
name, age = ('sas', 34)
# albo 
color = (222, 223, 224)
red, green, blue = color
# :)


#słowniki
print('Słowniki')

fortnite_dict = {
    'piotrek':'phenomenelik',
    'tomek':'monsterSASog',
    'ola':'ngSASog'
}
    
print(fortnite_dict)
print(piotrek)
print(tomek)
print(ola)

print(fortnite_dict.keys())
print(len(fortnite_dict))

# @ sas slowniki w miare ok, o czym zapomniales mianowicie -> odczyt wartosci ze slownika po kluczu
# czyli np
piotrek_user = fortnite_dict['piotrek']
# albo
tomek_user = fortnite_dict.get('tomek', 'DEFAULT') # get() pozwala podac defaultowa wartosc jesli klucz nie istnieje czyli:
jimmy_user = fortnite_dict.get('jimmy', 'notfound')
print('jimmy user', jimmy_user) # -> not found bo nie ma klucza jimmy


#Zadanie 2
"""zademonstruj dzialanie petli for (na dowolnym przykladzie - dodaj komentarz co ta petla robi)"""

print("-" * 10)
print('ZADANIE 2')
print(" ")

# poniższa pętla wyświetla kolejno graczy z listy fortnite
i = 0
for player in fortnite:
    i += 1
    print(str(i) + '. ' + player)

# @sas ok
    
#Zadanie 3
"""
zademonstruj dzialanie petli while (na dowolnym przykladzie - dodaj komentarz co ta petla robi)
"""

print("-" * 10)
print('ZADANIE 3 - TO DO')
print(" ")

fortnite_list = [
    'phenomenelik', 
    'monsterSASog', 
    'ngSASog', 
    'niepamietamnickupawcia'
]

# @sas !!! to sobie zrobimy razem online

#Wrócić do while bo zaćmienie

# Zadanie 4
print("-" * 10)
print('ZADANIE 4')
print(" ")
"""
opisz wlasnymi slowami roznice pomiedzy petla for i while  
"""

print('Zasadniczo te dwa rodzaje pętli różnią się tym, iż w WHILE możemy zadeklarować warunek kończący przekręcanie się pętli, tymczasie w FOR pętla kręci się do ostatniego elementu listy po której leci')

# @sas:
# i tak i nie, tak naprawde glowna roznica miedzy while i for jest to ze:
# WHILE moze byc petla nieskonczona np while True: print('i will never stop :)')
# FOR jest petla skonczona czyli for element in elements: print(element)  -> wykreci sie tyle razy ile jest elementow w liscie elements
# WAZNE!!! kazda z petli mozna przerwac instrukcja break np
for pet in ['dog', 'cat', 'rat']:
    if pet == 'cat': break
    print(pet)
# petla wypisze tylko 'dog' i sie przerwie
# Zadanie 5

print("-" * 10)
print('ZADANIE 5')
print(" ")

"""
zadeklaruj kilka zmiennych stosujac wyrazenia logiczne, mozesz przypisac do zmiennej od razu wynik wyrazenia albo kozystajac z klasycznego if'a   
"""

    
var1 = 'monsterSASog'
var2 = 'phenomenelik'
bool1 = False

if len(var1) > len(var2):
    bool1 = True
    print(bool1)
elif len(var1) < len(var2):
    print(bool1)
else:
    print('piotrek i tomek mają nicki tej samej długości')   

# @sas to teoretycznie ok ogolnie chodzi o wyrazenia logiczne czyli
a = 10
b = 10
if a + b == 20: print('correct')  # true
if a - b == 5: print('incorrect')  # false -> print nie zostanie wywolany

if a + b == 20 or a - b == 5: print('correct') # printnie bo pierwszy warunek spelniony a wyrazenie mowi ze cos or cosinnego
if a + b == 20 and a - b == 5: print('incorrect') # nie printnie bo drugi warunek jest nie spelniony
# itd itp

    

# Zadanie 6

"""
Utworz liste adresow email i przypisz do zmiennej   
"""
      
print("-" * 10)
print('ZADANIE 6')
print(" ")

email_list = [
    'phenomenelik@gmail.com',
    'piotr.menel@gmail.com',
    'pm.dev@yahoo.com'
]
# @sas ok
    
# Zadanie 7
"""
Wypisz ponumerowane adresy email z zad.6
"""

print("-" * 10)
print('ZADANIE 7')
print(" ")

i_mail = 0

for email in email_list:
    i_mail += 1
    print(f'{i_mail}. {email}')
    
# @sas - ok - mozna uzyc enumerate() tez => omowimy pozniej


# Zadanie 8
"""
Wypisz adresy email z zad.6 ale tylko takie ktore zawieraja okreslony ciag znakow (np. yolo)
"""

print("-" * 10)
print('ZADANIE 8 - TO DO')
print(" ")

# Zadanie 9
print("-" * 10)
print('ZADANIE 9 - TO DO')
print(" ")

# @sas: tutaj razem online sobie to omowimy

"""
opisz wlasnymi slowami czym jest funkcja, i w jaki sposob jest skonstuowana, jak jej uzyc   
"""
print('Nie wiem czy moje słowa dobrze oddadzą prawdziwą definicje funckji, ale... funkcja jest to operacja dzięki, której nie musimy powtarzać poszczególnych kilku operacji. Dzięki niej nie powtarzamy się i nasz kod jest DRY (don\'t repeat yourself)')

# @sas: tu mamy punkt do ktorego musimy sie cofnac i od tad isc do przodu ;)q

# Zadanie 10
print("-" * 10)
print('ZADANIE 10')
print(" ")

"""
zadeklaruj funkcje liczaca pole dowolnego trojkata
"""

def triangle_size(side, height):
    size = (side * height) / 2
    return size
    
print(triangle_size(6,6))
# @sas - ok - pomimo tego ze definicja z zad 9 kuleje ;)


# Zadanie 11
print("-" * 10)
print('ZADANIE 11')
print(" ")

"""
uzywajac funkcji z zad.10 przypisz do kilku zmiennych wynik obliczen pola trojkata dla roznych bokow   
"""

triangle1 = triangle_size(1,6)
print(triangle1)
triangle2 = triangle_size(20, 10)
print(triangle2)
triangle3 = triangle_size(5,5)
print(triangle3)

# @sas - ok :)

# Zadanie 12
print("-" * 10)
print('ZADANIE 12')
print(" ")

"""
zadeklaruj funkcje walidujaca dlugosc textu , jesli dlugosc jest przekroczona funkcja powinna podnosic wyjatek, w przypadku kiedy dlugosc jest poprawna powinna zwracac text ktory otrzymala na wejsciu
"""

def sms_validate():
    max_sms_len = 16
    sms = input('Napisz wiadomość sms: ')
    
    if len(sms) <= max_sms_len:
        print(' ')
        print('Wysłano wiadomość sms o treści:')
        print(sms)
    else:
        raise Exception('Zbyt długi sms do wysłania')

sms_validate()  # @ tu sobie omowimy i poprawimy, ogolnie troche jestem zaskoczony ze poprzednie zrobiles dobrze a to nie do konca ;)

# Zadanie 13
print("-" * 10)
print('ZADANIE 13')
print(" ")

"""
opisz wlasnymi slowami co to jest klasa
"""
# @sas - to moze poczekac

# Zadanie 14
print("-" * 10)
print('ZADANIE 14')
print(" ")

"""
opisz wlasnymi slowami co to jest obiekt
"""

print('Odpowiedzią na pytanie 13 i 14 jest zdanie: Każda klasa to obiekt, aczkolwiek nie każdy obiekt to klasa')
    
# @sas : nie :) - wrocimy do tego :)
    
    
    






