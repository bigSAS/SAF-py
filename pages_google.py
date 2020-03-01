from framework.action_framework import Page, Selector, Using


class Search(Page):
    def search_for(self, text: str):
        self.actions.element_provider.driver.get('https://google.pl')
        self.actions.type_text(Selector(Using.NAME, 'q'), text)
        self.actions.submit()
