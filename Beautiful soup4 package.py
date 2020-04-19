import requests as r #pakiet requests
from bs4 import BeautifulSoup #pakiet soup
url = 'https://www.pracuj.pl/praca/python;kw?rd=0'

page = r.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
element = soup.find(class_="results-header__offer-count-text-number")
print ('Liczba ofert pracy to:', element.text)