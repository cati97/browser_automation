from selenium import webdriver
from quotes_scraping_using_selenium.pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path='/home/cati/Desktop/driver/chromedriver')
chrome.get('http://quotes.toscrape.com/search.aspx')

page = QuotesPage(chrome)

authors = page.get_available_authors()
print(f'Choose one of these authors [{" | ".join(authors)}]')

author = input("Enter author name: ")
page.select_author(author)

tags = page.get_available_tags()  # returns a list of all tags available for specific author
print(f'Choose one of these tags: [{" | ".join(tags)}]')


tag = input("Enter tag name: ")
page.select_tag(tag)

page.search_button.click()

print(page.quotes)
