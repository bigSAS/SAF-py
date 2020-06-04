# Selenium
zanim zaczniesz tu cos odpalac to musisz wpisac w cmd (ctr + `) jesli nie ma (.env) to wpisujesz 
`. .env/bin/activate`
zeby odpalic testy wpisujesz:
`pytest -v ` wszystkie testy
`pytest -v plik.py` testy z pliku
`pytest -v plik.py::nazwa_funkcji` - odpala pojedynczy test
`pytest -v -m nazwa_markera` - odpala testy oznaczone markerem
