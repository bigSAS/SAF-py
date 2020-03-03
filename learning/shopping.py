"""
klasa klient:
- powinien miec koszyk
   - koszyk to lista stringow narazie czyli np koszyk to ['piwo', 'wino']
- powinien miec metode put_in_basket(item) czyli wrzucenie czegos do koszyka
- powinien miec metode buy() - jesli koszyk jest pusty to raise exception, jesli nie to print 'kupiles przedmioty ...'
"""


class Customer:
    def __init__(self, name):
        self.name = name
        self.basket = []
        
    def put_in_basket(self, item):
        if not isinstance(item, Product):
            raise Exception('item must be a Product instance!')
        self.basket.append(item)
        
    def buy(self):
        if len(self.basket) == 0:
            raise Exception('basket is empty! cannot buy')
        print('bought:')
        for i, item in enumerate(self.basket, 1):
            print(f'{i}. {item.name} - {item.price} PLN')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    beer = Product('Beer', 5)
    jellys = Product('Jellys', 3)
    customer = Customer('sas')
    customer.put_in_basket(beer)
    customer.put_in_basket(jellys)
    customer.buy()
        
