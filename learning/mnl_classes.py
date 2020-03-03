# todo: utworz klase reprezentujaca klienta w sklepie
# ..... powinien udostepniac metode buy() -> kupuje cos
# ..... powinien miec koszyk -> jesli koszyk jest pusty to nie moze nic kupic :)
# napisz to tak aby z definicji klasy mozna bylo rozkminic co mozna robic
# **** moglby miec portfel, a produkt wkladany do koszyka cene
# **** jesli ma zamalo siana w portfelu to nie moze kupic :)


class Customer:
    
    
    def __init___(self, basket, receipt, wallet):
        self.basket = basket
        self.receipt = receipt
        self.wallet = wallet
        self.got_money = wallet - receipt
        
    def buy_items(self):
        if self.got_money < 0:
            return 'Purchase refused, not enough money'
        elif basket <= 0:
            return 'Put items to your basket'
        else:
            return 'Thanks for buying good stuff. See you next time'
            

customer_1 = Customer(basket = 3, receipt = 300, wallet = 500)

print(Customer.buy_items(customer_1))

        
