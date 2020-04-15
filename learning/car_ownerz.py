def show_list(list):
    """funkcja wyświetla wszystkie elementy z listy"""
    for index, item in enumerate(list, 1):
        print(f'{index}. {item}')
        

def add_to_list(list, new_item):
    """funkcja dodaje element do listy"""
    list.append(new_item)
    return list
    
     
def find_item_in_list(list, find_param, param_value):
     """funkcja wyszukująca właściciela pojazdu z listy, po wskzaniu parametru wyszukania i jego wartości, jeżeli pojazd nie zostanie znaleziony zwraca błąd"""
     found_item = None
     error = None
     for item in list:
         if item.get(find_param) == param_value:
             try:
                 found_item = item
             except Exception(f'item with param: {find_param} = value: {param_value} - not found') as e:
                 error = f'ERROR!\n{e}'
     return found_item or error


def remove_item_from_list(list, find_remove_param, remove_param_value):
    """funkcja usuwa wskzanego wskazany element z listy"""
    remove_item = find_item_in_list(list, find_remove_param, remove_param_value)
    list.remove(remove_item)
    return list
    
def update_item(list, find_param, param_value, updated_data):
    """funkcja aktualizująca dane"""
    remove_item_from_list(list, find_param, param_value)
    add_to_list(list, updated_data)
    return list
            

# lista właścicieli pojazdów
car_ownerz = [
    {
        'name': 'Piotrek',
        'age': 32,
        'phone': '501-052-396',
        'car': {
            'make': 'Saab',
            'model': '9-3',
            'model_year': 2007,
            'est_price': 12500
        }
    },
    {
        'name': 'Wojtek',
        'age': 68,
        'phone': None,
        'car': {
            'make': 'Kia',
            'model': 'Sportage',
            'model_year': 2015,
            'est_price': 64000
        }
    },
    {
        'name': 'Tomek',
        'age': 35,
        'phone': None,
        'car': None
    },
]

# lista samochodów
carz = [
    {
        'make': 'Jeep',
        'model': 'Grand Cherokee SRT/8',
        'model_year': 2020,
        'est_price': 360000 
    },
    {
        'make': 'Mercedes',
        'model': 'E-Class',
        'model_year': 2008,
        'est_price': 50000 
    },
]


print('Wywołania funkcji:')
print('')
print('')
        
print('1. POKAŻ WSZYSTKICH WŁAŚCICIELI POJAZDÓW')
print('')
show_list(car_ownerz)
print('-' * 20)
print('')


print('2. POKAŻ WSZYSTKIE POJAZDY')
print('')
show_list(carz)
print('-' * 20)
print('')


print('3. DODAJ WŁAŚCICIELA')
print('')
new_owner = {
        'name': 'Mateusz',
        'age': 30,
        'phone': None,
        'car': {
            'make': 'Ford',
            'model': 'Ka',
            'model_year': 2001,
            'est_price': 4000
    }
}
new_owner1 = {
        'name': 'Gosia',
        'age': 37,
        'phone': '606-646-202',
        'car': None
}
new_owner2 = {
        'name': 'Zbynio',
        'age': 32,
        'phone': None,
        'car': {
            'make': 'BMW',
            'model': '3-Series Cabrio',
            'model_year': 2010,
            'est_price': 49000
    }
}

add_to_list(car_ownerz, new_owner)
print(new_owner)
print('')
show_list(car_ownerz)
print('-' * 20)
print('')


print('4. ZNAJDŹ WŁAŚCICIELA POJAZDU')
print('')
print(find_item_in_list(car_ownerz, 'name', 'Piotrek'))
#print(find_car_owner(car_ownerz, 'name', 'Rumcajs'))
print('-' * 20)
print('')


print('5. USUŃ WŁAŚCICIELA')
print('')
remove_item_from_list(car_ownerz, 'name', 'Piotrek')
print('')
show_list(car_ownerz)
#remove_from_car_ownerz(car_ownerz, 'name', 'Rumcajs')
print('-' * 20)
print('')


print('6. ZNAJDŹ POJAZD W LIŚCIE')
print('')
print(find_item_in_list(carz, 'model', 'Grand Cherokee SRT/8'))
print('-' * 20)
print('')


print('6. DODAJ POJAZD')
print('')
new_kia = {
        'make': 'Kia',
        'model': 'Sportage',
        'model_year': 2019,
        'est_price': 115000
}

add_to_list(carz, new_kia)
show_list(carz)
print('-' * 20)
print('')


print('7. USUŃ POJAZD Z LISTY')
print('')
remove_item_from_list(carz, 'make', 'Jeep')
print('')
show_list(carz)
print('-' * 20)
print('')


print('8. AKTUALIZUJ DANE POJAZDU')
print('')
new_kia_data = {
        'make': 'Kia',
        'model': 'Sportage',
        'model_year': 2020,
        'est_price': 115000
}
update_item(carz, 'make', 'Kia', new_kia_data)
show_list(carz)
print('-' * 20)
print('')


