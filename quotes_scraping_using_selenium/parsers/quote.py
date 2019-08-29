from quotes_scraping_using_selenium.locators.quotes_locators import QuoteLocators as Ql


class QuoteParser:
    """
    Given a specific div, return content
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def author(self):
        locator = Ql.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def content(self):
        locator = Ql.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = Ql.TAGS
        return [t.string for t in self.parent.find_elements_by_css_selector(locator)]
