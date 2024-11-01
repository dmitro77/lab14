import requests
from bs4 import BeautifulSoup

address = input("Enter website address: ")

content = requests.get(address).content
soup = BeautifulSoup(content, 'html.parser')

hrefList = soup.find_all('a')

with open("task1/allHyperlinks.txt", "w") as f:
    finalString = ""
    for href in hrefList:
        finalString += str(href.get('href')) + "\n"
    f.write(finalString)
