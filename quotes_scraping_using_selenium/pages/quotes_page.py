from typing import List
from selenium.webdriver.support.ui import Select

from quotes_scraping_using_selenium.locators.quotes_page_locators import QuotesPageLocators
from quotes_scraping_using_selenium.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):

        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quotes = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quotes]

    @property
    def author_dropdown(self) -> Select:
        locator = QuotesPageLocators.AUTHOR_DROPDOWN
        author = self.browser.find_element_by_css_selector(locator)
        return Select(author)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tag_dropdown(self) -> Select:
        locator = QuotesPageLocators.TAG_DROPDOWN
        element = self.browser.find_element_by_css_selector(locator)
        return Select(element)

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)
