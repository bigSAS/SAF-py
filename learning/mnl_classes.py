# todo: utworz klase reprezentujaca klienta w sklepie
# ..... powinien udostepniac metode buy() -> kupuje cos
# ..... powinien miec koszyk -> jesli koszyk jest pusty to nie moze nic kupic :)
# napisz to tak aby z definicji klasy mozna bylo rozkminic co mozna robic
# **** moglby miec portfel, a produkt wkladany do koszyka cene
# **** jesli ma zamalo siana w portfelu to nie moze kupic :)

#klasa klient:
#- powinien miec koszyk
#- koszyk to lista stringow narazie czyli np koszyk to ['piwo', 'wino']
#- powinien miec metode put_in_basket(item) czyli wrzucenie czegos do koszyka
#- powinien miec metode buy() - jesli koszyk jest pusty to raise exception, jesli nie to print 'kupiles przedmioty ...'


class Customer:
    
    
    def __init__(self, name):
        self.name = name
        self.basket = []
        
    def put_in_basket(self, item):
        self.basket.append(item)
        
    def buy(self):
        if len(self.basket) == 0:
            raise Exception('Your basket is empty')
        else:
            print('Transaction in progress... ... ... .. .. .. . . . ')
            print('You bought:')
            i = 1
            for product in self.basket:
                print(f'{i} {product}')
                i += 1
                
customer = Customer('Menel')
customer.put_in_basket('5g lemon haze (CBD only)')
customer.put_in_basket('2g white widow (CBD only)')
customer.put_in_basket('5g strawberry kush (CBD only)')
customer.buy()

print('done. :)')
                    

"""
class Customer:
    def __init__(self, name):
        self.name = name
        self.basket = []
        
    def put_in_basket(self, item):
        self.basket.append(item)
        
    def buy(self):
        if len(self.basket) == 0:
            raise Exception('basket is empty! cannot buy')
        print('bought:')
        for i, item in enumerate(self.basket, 1):
            print(f'{i}. {item}')        
 """          

