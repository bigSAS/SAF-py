
class Car:

    
    def __init__(self, make, model, model_year, engine, power, price):
        self.make: str = make
        self.model: str = model
        self.model_year: int = model_year
        self.engine: int = engine
        self.power: int = power
        self.price: int = price
    
    def __str__(self):
        return f'Car -> make: {self.make}, model: {self.model}, model year: {self.model_year}, engine: {self.engine}, power: {self.power}, price: {self.price}.'
    

class Expectations:
    def __init__(self, engine, power, price):
        self.engine: str = engine
        self.power: int = power
        self.price: int = price
        
    def __str__(self):
        return f'Expectations: engine: {self.engine}, min power: {self.power}, max price: {self.price})'


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
        print('customer: ', customer.expectations)
        result = []
        for car in  self.cars:
            if self.correct_car(car, customer.expectations):
                result.append(car)
        return result

    @staticmethod
    def correct_car(car, expectations):
        return int(car.power) >= int(expectations.power) and int(car.price) <= int(expectations.price)
        
class Discount:
    
    
    def __init__(self, car):
        self.car = car
        
    def carwizards_price(self):
        discounts = [0.05, 0.10, 0.20]
        if self.car.price > 50000 and self.car.price < 60000:
            new_price = self.car.price - (self.car.price * discounts[0])
            return new_price
            
        elif self.car.price > 60000 and self.car.price < 65000:
            new_price = self.car.price - (self.car.price * discounts[1])
            return new_price
            
        else:
            return 'Something went wrong call administrator 501052396 :('
            
class Ask_for_contact:
    
    
    def __init__(self, car, customer, phone):
        self.car = car
        self.customer = customer
        self.phone = phone
        
    def __str__(self):
        return f'Our client is looking for {self.car.make} {self.car.model}, please call him: {self.customer.name} phone: {self.phone}'       
        
if __name__ == "__main__":
    
    polo = Car(
        'VW',
        'Polo',
        20,
        'PB',
        80,
        60000,
        )
        
    fabia = Car(
        'Skoda',
        'Fabia',
        20,
        'PB',
        95,
        60000,
        )
      
    yaris = Car(
        'Toyota',
        'Yaris',
        20,
        'PB',
        111,
        61000,
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
        100,
        65000
    )
    
    customer_1 = Customer(c1_name, c1_ex)
    ask_for_contact = Ask_for_contact(yaris, customer_1, '501-052-396')    
    print(customer_1)
    
    found_cars = wizard.find_cars(customer_1)
    print('found')
    for car in found_cars:
        print(car)
        print(f'If you buy a car with carwizard you will pay {Discount(car).carwizards_price()}')
        
    print(ask_for_contact)
          
