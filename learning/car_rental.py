# klasa główna
class Car_rental:
    def __init__(self, client, rent, car_category):
        self.client = client
        self.rent = rent
        self.car_category = car_category
    

#klasa klienta
class Client:
    def __init__(self, name):
        self.name = name
    
    
#klasa wypozyczenie
class Rent:
    def __init__(self, client, rent_start, rent_end, car, rent_price, payment_upfront)
    
    
    
#klasa samochodu
class Car:
    
    def __init__(self, index, make, model, car_category):
        
    self.index = index
    self.make = make
    self.model = model
    self.car_category = car_category
        
class Car_storage:
    def __init__(self, car):
        self.car = car


#kategoriac samochodu
class Car_category:
