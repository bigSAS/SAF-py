class Car:
    
    def __init__(self, car_id, make, model, price_day, category):
        self.car_id: int = car_id
        self.make: str = make
        self.model: str = model
        self.price_day: int = price_day
        self.category: str = category
        
    def __str__(self):
        return f'id: {self.car_id}, make: {self.make}, model: {self.model}, price: {self.price_day}/day, category: {self.category}'
        
        
class Customer_expec:
    def __init__(self, price_day, category):
        self.price_day = price_day
        self.category = category
    
    def __str__(self):
        return f"Customer's expectations: max price: {self.price_day}/day', category: {self.category}"
       
    
    
    
class Customer:
    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name
    
    def give_login(self):
        login = f'{self.first_name}.{self.last_name}'
        return login
        
    def __str__(self):
        return f'first name: {self.first_name}, last name: {self.last_name}, login: {self.give_login().lower()}'
        


    
    
if __name__ == '__main__':
    
    polo = Car(1, 'VW', 'Polo', 150, 'Basic')
    fabia = Car(2, 'Skoda', 'Fabia', 135, 'Basic')
    ibiza = Car(3, 'Seat', 'Ibiza', 140, 'Basic')
    passat = Car(4, 'VW', 'Passat', 250, 'Premium')
    a4 = Car(5, 'Audi', 'A4', 280, 'Premium')
    optima = Car(6, 'Kia', 'Optima', 230, 'Premium')
    a8 = Car(7, 'Audi', 'A8', 500, 'VIP')
    bmw_7 = Car(8, 'BMW', '740i', 550, 'VIP')
    merc_s = Car(9, 'Mercedes', 'S-Class', 600, 'VIP')
    print(polo)
    print(fabia)    
    print(ibiza)
    print(passat)
    print(a4)
    print(optima)
    print(a8)
    print(bmw_7)
    print(merc_s)
    
    customer1_expec = Customer_expec(400, 'Premium')
    customer2_expec = Customer_expec(100, 'Basic')
    customer3_expec = Customer_expec(570, 'VIP')   
    print(customer1_expec)
    print(customer2_expec)
    print(customer3_expec)
    
    customer1 = Customer('Piotr', 'Menel')
    customer2 = Customer('Małgorzata', 'Żukowska')
    customer3 = Customer('Tomasz', 'Majk')
    print(customer1)
    print(customer2)
    print(customer3)
        
