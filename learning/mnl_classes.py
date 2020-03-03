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
            raise Exception('basket is empty! cannot buy')
        print('bought:')
        for i, item in enumerate(self.basket, 1):
            print(f'{i}. {item}')
            
            
class Product:
    def __initi__(self, prod_name, price):
        self.prod_name = prod_name
        self.price = price

    def test(self):
        if len(prod_name) > 0:
            print('good')

if __name__ == '__main__':
    
#    prod_1 = Product('beer', 5)
#    prod_1.test()
    product.test('beer', 5)
    customer = Customer('sas')
    customer.put_in_basket('beer')
    customer.put_in_basket('wine')
    customer.put_in_basket('vodka')
    customer.buy()
