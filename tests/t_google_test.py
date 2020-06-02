import pytest
from framework.action_framework import Actions
from framework.conditions import XpathExists
from framework.selector import Selector, Using
from pages.google.pages_google import Search


@pytest.mark.debug
def test_google_search(actions: Actions):
    """
    Szukaj z uzyciem samych actions'ow
    Mozesz dodawac funkcje jakie dusza zapragnie i wywolywac selenium poprzez actions,
    tam jest pod spodem duzo ogarniete
    czyli robisz np:
    actions.click(selector)
    actions.type_text(selector, text)
    actions.submit()
    itd. omowimy se to
    """
    driver = actions.element_provider.driver
    search_text = 'dr dissrespect'  # tekst do wpisania
    actions.element_provider.driver.get('https://google.pl')  # otworz gugle
    search_input_selector = Selector(Using.NAME, 'q')  # definiujesz kontrolke (to se omowic bardziej mozemy)
    actions.type_text(search_input_selector, search_text)  # wpisz text
    actions.submit()  # submit formularza
    search_result_exist_xpath = "//div[@class='g']"  # xpath do poczekania
    actions.wait_for(XpathExists(search_result_exist_xpath))  # jesli ten xpath istnieje to kolejny ekran sie zaladowal

    title = driver.title  # odczytaj tytul stronki
    assert search_text in title, f"tytul strony powinien zawierac: {search_text}"  # asercja

@pytest.mark.pop
def test_google_search_with_page_object(actions: Actions):
    """
    Szukaj z uzyciem page objecta - to se pokminisz z czasem - prosty patern
    """
    search_text = 'dr dissrespect'
    search_page = Search(actions)  # tworze obiekt pagea
    search_page.search_for(search_text)  # wywoluje na nim metode szukaj
    driver = actions.element_provider.driver
    title = driver.title  # odczytaj tytul stronki
    assert search_text in title, f"tytul strony powinien zawierac: {search_text}"  # asercja
