"""
print('hello nigger')
print('klaski na levelu pussih dzifko 1on1')
print('-' * 80)


# ! definicja klasy lvl pussy
# ! zawsze keyword class
# ! potem nazwa klasy z duzej litery
# ! potem konstruktor (__init__) - konstruktor jest metodą (funkcją) - *metoda to funkcja na obiekcie (zawsze self jako pierwszy parametr!!!)*

class Car:
    Klasa reprezentujaca samochod :)
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __str__(self):
        return f'car: {self.make} - {self.model}'

mustand_dict = {
    'make': 'ford',
    'model': 'mustang'
}

print('mustang dict')
print(mustand_dict)
print(mustand_dict['make'])

mustang_obj = Car(make='ford', model='mustang')
print('mustang: ', mustang_obj)
print(mustang_obj.make)

# todo: @zad: postaraj sie odtworzyc to samo dla szukania samochodu w liscie jak ze slownikem
# ! tylko ze lista nie jest juz listą słowników tylko obiektów klasy Car
# ! mile widziane obsluga wyjatkow, np Car not found
# :) hint -> mozesz sobie zmixowac logike, bo znasz atrybuty klasy Car (make, i model)
# czyli mozesz sobie szukac np po make albo po model albo po jednym i drugim
# mozesz tez skipnac przyjmowanie cars jako parametr :)

CARS = [
    Car(make='??', model='??'),
    Car(make='??', model='??'),
    Car(make='??', model='??')
]

# ! -> znajdz wszystkie ktore pasuja i oddaj liste
# ! -> jesli nie znajdzie nic to oddaje pusta liste
def get_cars_by_make(make: str) -> list: DONE
    pass

def get_cars_by_model(make: str) -> list: DONE
    pass

def get_cars_by_make_and_model(make: str, model: str) -> list: DONE
    pass

# todo: mozesz tez zrobic warianty dla get_car -> oddaj jeden obiekt
# ! hint: wystarczy ze oddasz pierwszy, ktory pasuje (nawet jesli by wiecej pasowalo)
# ! -> jesli nie znajdzie to podnies wyjatek CarNotFoundHommie :)
def get_car_by_make(make: str) -> Car: DONE
    pass

def get_car_by_model(make: str) -> Car: DONE
    pass

def get_car_by_make_and_model(make: str, model: str) -> Car: DONE
    pass
    
"""

class CarNotFoundHommie(Exception):
    """klasa reprezentująca błąd występujący podczas wywołania funckji"""
    pass


class Car:
    """klasa reprezentująca samochód, posiada 3 parametry markę->make, nazwę modelu->model, oraz rocznik->year"""
    def __init__(self, make: str, model: str, year: int):
        self.make: str = make
        self.model: str = model
        self.year: int = year
        
    def __str__(self):
        return f'Car -> make: {self.make}, model: {self.model}, year: {self.year}'
 
        
class Owner:
    """Klasa reprezentująca właścicela pojazdu"""
    def __init__(self, name: str, email: str, age: int, car: object):
        self.name: str = name
        self.email: str = email
        self.age: int = age
        self.car: object = car
        
    def __str__(self):
        return f'Owner -> name: {self.name}, e-mail: {self.email}, age: {self.age}, {self.car}'
               

# ! -> znajdz wszystkie ktore pasuja i oddaj liste
# ! -> jesli nie znajdzie nic to oddaje pusta liste
def get_cars_by_make(cars_list: list, make: str):
    """funkcja zwracająca listę samochodów wskazanej wcześniej marki"""
    cars = []
    for car in cars_list:
        if car.make == make:
            cars.append(car)
    return cars
        

def get_cars_by_model(cars_list: list, model: str):
    """funkcja zwracajaąca listę samochodów wskazanego wcześniej modelu"""
    cars = []
    for car in cars_list:
        if car.model == model:
            cars.append(car)
    return cars

def get_cars_by_make_and_model(cars_list: list, make: str, model: str):
    """funkcja zwracająca listę samochodów o wskazanym modelu i marce"""
    cars = []
    for car in cars_list:
        if car.model == model and car.make == make:
            cars.append(car)
    return cars

# todo: mozesz tez zrobic warianty dla get_car -> oddaj jeden obiekt
# ! hint: wystarczy ze oddasz pierwszy, ktory pasuje (nawet jesli by wiecej pasowalo)
# ! -> jesli nie znajdzie to podnies wyjatek CarNotFoundHommie :)
def get_car_by_make(cars_list: list, make: str):
    """funkcja zwracająca samochód wskazanej marki, pierwszy odnaleziony"""
    found_car = None
    for car in cars_list:
        if car.make == make:
            found_car = True
            break
    if found_car is None:
       raise CarNotFoundHommie(f'Car {make} not found')
    return car
        

def get_car_by_model(cars_list: list, model: str):
    """funkcja zwracająca wskazany model samochodu, pierwszy odnaleziony"""
    found_car = None
    for car in cars_list:
        if car.model == model:
            found_car = True
            break
    if found_car is None:
       raise CarNotFoundHommie(f'Car {model} not found')
    return car

def get_car_by_make_and_model(cars_list: list, make: str, model: str):
    """funkcja zwracająca samochodów wskazanej marki i modelu, pierwszy odnaleziony"""
    found_car = None
    for car in cars_list:
        if car.model == model and car.make == make:
            found_car = True
            break
    if found_car is None:
       raise CarNotFoundHommie(f'Car {make} {model} not found')
    return car


def print_list(list):
    """funkcja zwraca elementy listy"""
    for item in list:
        print(item)

saab_obj = Car('Saab', '9-3', 2007)
merc_obj = Car('Mercedes-Benz', 'E-Class', 2010)
kia_obj = Car('Kia', 'Sportage', 2019)
kia_obj1 = Car('Kia', 'Sportage', 2015)
honda_obj = Car('Honda', 'Jazz', 2002)
honda1_obj = Car('Honda', 'NSX', 2001)
honda2_obj = Car('Honda', 'Civic', None)
honda3_obj = Car('Honda', 'Accord', 2020)



cars_list = [saab_obj, merc_obj, kia_obj, kia_obj1, honda_obj, honda1_obj, honda2_obj, honda3_obj]
    
menel = Owner('Piotrek', 'phenomenelik@gmail.com', 32, saab_obj)
dominika = Owner('Dominika', None, 23, honda_obj)
wojtek = Owner('Wojtek', None, None, kia_obj)
mati = Owner('Mateusz', 'smomat@o2.pl', 30, merc_obj)

ownerz_list = [menel, dominika, wojtek, mati]

print('get_cars_by_make')
print('')
got_cars_by_make = get_cars_by_make(cars_list, make='Honda')
print_list(got_cars_by_make)
print('-'*10)
print('')

print('get_cars_by_make')
print('')
got_cars_by_make = get_cars_by_make(cars_list, make='Ferarri')
print_list(got_cars_by_make)
print('-'*10)
print('')

print('get_cars_by_model')
print('')
got_cars_by_model = get_cars_by_model(cars_list, model='Sportage')
print_list(got_cars_by_model)
print('-'*10)
print('')

print('get_cars_by_make_model')
print('')
got_cars_by_make_model = get_cars_by_make_and_model(cars_list, make='Honda', model='Jazz')
print_list(got_cars_by_make_model)
print('-'*30)
print('')

print('get_car_by_make')
print('')
got_car_by_make = get_car_by_make(cars_list, make='Honda')
print(got_car_by_make)
print('-'*10)
print('')

print('get_car_by_make - not found')
print('')
try:
    got_car_by_make_not_found = get_car_by_make(cars_list, make='SHIT')
    print(got_car_by_make_not_found)
except CarNotFoundHommie as ex:
    print(f'{ex}')
print('-'*10)
print('')

print('get_car_by_model')
print('')
got_car_by_model = get_car_by_model(cars_list, model='Sportage')
print(got_car_by_model)
print('-'*10)
print('')

print('get_car_by_model - not found')
print('')
try:
    got_car_by_model_not_found = get_car_by_model(cars_list, model='SHIT')
    print(got_car_by_make_not_found)
except CarNotFoundHommie as ex:
    print(f'{ex}')
print('-'*10)
print('')

print('get_car_by_make_model')
print('')
got_car_by_make_model = get_car_by_make_and_model(cars_list, make='Honda', model='Jazz')
print(got_car_by_make_model)
print('-'*10)
print('')

print('get_car_by_make_model - not found')
print('')
try:
    got_car_by_make_model = get_car_by_make_and_model(cars_list, make='Porsche', model='Panamjera')
    print(got_car_by_make_model)
except CarNotFoundHommie as ex:
    print(ex)
print('-'*10)
print('')