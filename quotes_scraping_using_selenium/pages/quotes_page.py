from quotes_scraping_using_selenium.locators.quotes_page_locators import QuotesPageLocators
from quotes_scraping_using_selenium.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotes = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quotes]
