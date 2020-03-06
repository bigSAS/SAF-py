class Car:

    
    def __init__(self, make, model, engine, power):
        
        self.make: str = make
        self.model: str = model
        self.engine: str = engine
        self.power: str = power
    
    def __str__(self):
        
        return f'Car -> make: {self.make}, model: {self.model}, engine: {self.engine}, power: {self.power}.'
        
        
class Chip_tune:
    
    
    def __init__(self, car):
        
        self.car = car
        
    def add_power(self):
        new_power = 0
        if int(self.car.power) > 0:
             new_power = int(self.car.power) * 0.2 + int(self.car.power)
             return new_power
            
        else:
            raise Exception('Invalid power')

if __name__ == "__main__":
    
    
    saab_93 = Car(
        'Saab',
        '9-3',
        'Diesel',
        '120'
        )
        
    vw_golf = Car(
        'VW',
        'Golf',
        'Diesel',
        '105'
        )
        
    chip_saab_93 = Chip_tune(saab_93)
    new_saab_power = str(chip_saab_93.add_power())
    
    print(f'{saab_93.make} {saab_93.model} engine power tuned to {new_saab_power}')
    
    
    
    chip_vw_golf = Chip_tune(vw_golf)
    new_golf_power = str(chip_vw_golf.add_power())
    print(f'{vw_golf.make} {vw_golf.model} engine power tuned to {new_golf_power}')
    
    
    
    

    
    
    
    
    
    
    
    
