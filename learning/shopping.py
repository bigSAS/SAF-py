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
        self.basket.append(item)
        
    def buy(self):
        if len(self.basket) == 0:
            raise Exception('basket is empty! cannot buy')
        print('bought:')
        for i, item in enumerate(self.basket, 1):
            print(f'{i}. {item}')


if __name__ == '__main__':
    customer = Customer('sas')
    customer.put_in_basket('beer')
    customer.buy()
        
