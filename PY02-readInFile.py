import requests
from bs4 import BeautifulSoup

with open("../Javascript/carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print (soup.prettify())