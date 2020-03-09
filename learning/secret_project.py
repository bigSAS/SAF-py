import types

class Car:

    
    def __init__(self, make, model, model_year, engine, power, price):
        # celowo dałem str, docelowo chciałem wartości wyszukiwania zrobić inputem
        self.make: str = make
        self.model: str = model
        self.model_year: str = model_year
        self.engine: str = engine
        self.power: str = power
        self.price: str = price
    
    def __str__(self):
        
        return f'Car -> make: {self.make}, model: {self.model}, model year: {self.model_year}, engine: {self.engine}, power: {self.power}, price: {self.price}.'
    

class Customer:
    
    
    def __init__(self, name, engine, power, price):
        
        self.name: str = name
        self.engine: str = engine
        self.power: str = power
        self.price: str = price

    def __str__(self):
        
        return f'Customers choice -> name: {self.name}, engine: {self.engine}, power: {self.power}, price: {self.price}.'
        
class CarWizard:
    
    
    def __init__(self, car, customer):
        
        self.listed_cars = []
        self.price_in_range = False

        
    def check_price(self, car, customer):
        
    
    
    
if __name__ == "__main__":
    
    polo = Car(
        'VW',
        'Polo',
        '20',
        'PB',
        '80',
        '60000',
        )
        
    fabia = Car(
        'Skoda',
        'Fabia',
        '20',
        'PB',
        '95',
        '60000',
        )
      
    yaris = Car(
        'Toyota',
        'Yaris',
        '20',
        'PB',
        '111',
        '57000',
        )
        
    cars_list = [
        polo,
        fabia,
        yaris
        ]
        
    customer_1 = Customer(
        'Jan',
        'PB',
        '100',
        '65000'
        )
        
    customer_2 = Customer(
        'Tomek',
        'ON',
        '150',
        '50000'
        )
        
    customer_3 = Customer(
        'Piotrek',
        'PB',
        '80',
        '70000'
        )
        
    customer_4 = Customer(
        'Gosia',
        'PB',
        '80',
        '59000'
        )    
            
    print(polo)
    print(fabia)
    print(yaris)

    print(customer_1)
    print(customer_2)
    print(customer_3)
    print(customer_4)

    

