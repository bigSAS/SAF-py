""" :) """
"""
Przykladowa klasa w python'ie
"""

class Car:
    """ Klasa reprezentujaca samochod """
    def __init__(self, manufacturer, model, year = '2000'):
        self.manufacturer: str = manufacturer
        self.model: str = model
        self.model_year: str = year
        self.driver: str = None
        
    
    def drive(self):
        if not self.driver: raise Exception('NO DRIVER!!!')
        print(self.driver + ' is driving :)')
        
    def enter(self, person: str):
        self.driver = person
    
    def __str__(self):
        return f'Car => man: {self.manufacturer}, mod: {self.model}, year: {self.model_year}'


mustang = Car(
    manufacturer="ford",
    model="mustang",
    year="2020"
)

#mustang.enter('mnl')

# tak btym napisal jak bym nie byl w stanie stwierdzic czy ktos wsiadl
try:
    mustang.drive()
except:
    mustang.enter('default driver')
    mustang.drive()



print(mustang)
mustang.manufacturer = 'Fordingo'
#mustang.model = 'Mustang'
#mustang.model_year = '2020'
#print(mustang)





















print('----'*5)

class Car_S:
    owner = 'mnl'
    """ Klasa reprezentujaca samochod """
    def __init__(self):
        self.manufacturer: str = ''
        self.model: str = ''
        self.model_year: str = ''
    def __str__(self):
        return f'Car => man: {self.manufacturer}, mod: {self.model}'

car_s = Car_S()
car_s.manufacturer = 'dd shit'
print(car_s)
