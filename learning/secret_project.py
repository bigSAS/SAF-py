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
    

class Expectations:
    def __init__(self, engine, power, price):
        self.engine: str = engine
        self.power: str = power
        self.price: str = price
        
    def __str__(self):
        return f'Exp(e: {self.engine}, po: {self.power}, pr: {self.price})'


class Customer:
    def __init__(self, name, expectations):
        self.name: str = name
        self.expectations = expectations

    def __str__(self):
        
        return  f'Customer: {self.name} => exp: {self.expectations}'
        
class CarWizard:
    def __init__(self, cars):
        self.cars = cars

    def find_cars(self, customer):
        print('searching')
        print('customer exp:', customer.expectations)
        result = []
        for car in  self.cars:
            if self.correct_car(car, customer.expectations):
                result.append(car)
        return result

    @staticmethod
    def correct_car(car, expectations):
        return int(car.power) >= int(expectations.power) and int(car.price) <= int(expectations.price)
    
    
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
        
    wizard = CarWizard(cars_list)
    
    c1_name = 'Jan'
    c1_ex = Expectations(
        'PB',
        '100',
        '65000'
    )
    customer_1 = Customer(c1_name, c1_ex)

            
    print(polo)
    print(fabia)
    print(yaris)

    print(customer_1)
    
    found_cars = wizard.find_cars(customer_1)
    print('found')
    for car in found_cars:
        print(car)
        
    pow_in = int(input('power?'))
    
    print(isinstance(pow_in, int))
    
    

