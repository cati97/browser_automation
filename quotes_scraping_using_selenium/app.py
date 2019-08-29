from selenium import webdriver
from quotes_scraping_using_selenium.pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path='/home/cati/Desktop/driver/chromedriver')
chrome.get('http://quotes.toscrape.com/search.aspx')

page = QuotesPage(chrome)

author = input("Enter author name: ")
page.select_author(author)

tag = input("Enter tag name: ")
page.select_tag(tag)
