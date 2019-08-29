from selenium import webdriver
from quotes_scraping_using_selenium.pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path='/home/cati/Desktop/driver/chromedriver')
chrome.get('http://quotes.toscrape.com/search.aspx')

page = QuotesPage(chrome)

for q in page.quotes:
    print(q)
