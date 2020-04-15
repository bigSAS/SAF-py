# todo: @zad - napisz sobie jakas funkcje ktora bedzie rzucac wyjatkiem jesli nie wykona sie poprawnie
# ! dzielenie -> jesli masz dzielenie przez 0 to rzuc wyjatek DivisionByZeroh
# ! nastepnie wywolaj funkcje dwa razy, raz poprawnie raz nie i obsluz wyjatek (try catch)
# ? jesli ci sie chce to pokombinuj z bardziej skomplikowanym casem :)

class DivisionByZeroh(Exception): pass

def division(dzielna, dzielnik):
    iloraz = None
    if dzielna > 0 and dzielnik > 0:
        iloraz = dzielna / dzielnik
    if iloraz is None:
        raise DivisionByZeroh(f'Człeniu nie idzie używać zer w dzieleniu')
    return iloraz

print(division(dzielna=2, dzielnik=2))
print(division(dzielna=100, dzielnik=10))    
try:
    print(division(dzielna=2,dzielnik=0))
except DivisionByZeroh as e:
    print(f'error: {e}')
    
try:
    print(division(dzielna=0,dzielnik=2))
except DivisionByZeroh as e:
    print(f'error: {e}')
