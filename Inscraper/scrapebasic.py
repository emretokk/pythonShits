from bs4 import BeautifulSoup
import requests

page_source = requests.get("https://www.instagram.com/emin_kacmaz_72")
soup = BeautifulSoup(page_source.text,"html.parser")
print(soup.prettify())