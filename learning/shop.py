""" SHOP """
# todo:


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.basket = Basket()
    
    def put_product_in_basket(self, product):
        self.basket.put_in(product)
    
    def put_product_out_of_basket(self, product):
        self.basket.put_out(product)
    
    def read_total_product_price(self):
        print('my basket has total price: ', self.basket.total_price())
    
    def can_afford(self) -> bool:
        # todo: moge kupic tylko wtedy jesli mam wystarczajaco kasy w portfelu
        return self.wallet.amount >= self.basket.total_price()
    
    def __str__(self):
        return f'{self.name}: {self.wallet}, {self.basket}'


class Wallet:
    def __init__(self, amount = 0):
        self.amount = amount
    
    def __str__(self):
        return str(self.amount) + ' PLN'

class Basket:
    def __init__(self):
        self.products = []
        
    def put_in(self, product):
        self.products.append(product)
    
    def put_out(self, product):
        self.products.remove(product)
        
    def total_price(self) -> int:
        sum = 0
        for product in self.products:
            sum += product.price
        
        return sum
    
    def __str__(self):
        product_names = ', '.join([p.name for p in self.products])
        return '[[ ' + product_names + ' ]]'


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'{self.name} - {self.price} PLN'





if __name__ == '__main__':
    beer = Product('beer', 5)
    cigz = Product('cigaretes', 15)
    print('beer', beer)
    print('cigz', cigz)
    
    basket = Basket()
    print('\nbasket', basket)
    print('put in beer')
    basket.put_in(beer)
    print('basket', basket)
    print('put out')
#    basket.put_out(beer)
    print('basket', basket)
    
    empty_wallet = Wallet()
    full_wallet = Wallet(500)
    
    print('\nwallets')
    print('empty', empty_wallet)
    print('full', full_wallet)
    
    print('\ncustomer')
    jimmy = Customer(
        name='jimmy',
        wallet=Wallet(100)
    )
    
    print('before put in basket')
    print(jimmy)
    print('after put in basket')
    print(jimmy)
    print('add new product to jimmys basket')
    jimmy.put_product_in_basket(Product('dildo', 100))
    jimmy.put_product_in_basket(Product('dildo', 100))
    print(jimmy)
    jimmy.read_total_product_price()
    print(jimmy.can_afford())
