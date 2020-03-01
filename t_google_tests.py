from framework.action_framework import Actions

from pages_google import Search


def test_google_search(actions: Actions):
    search_text = 'dr dissrespect'
    search_page = Search(actions)
    search_page.search_for(search_text)
    assert search_text in actions.element_provider.driver.title
    hello = actions.execute_js('return true;')
    assert hello.lower() == 'true'
