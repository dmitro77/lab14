import requests
from bs4 import BeautifulSoup
import json

content = requests.get("https://dmitro77.github.io/lab14/").content
soup = BeautifulSoup(content, 'html.parser')
mailList = []
for tag in soup.find_all('li'):
    mailList.append(tag.text.strip())

countedEmailDomains = dict()
for email in mailList:
    domain = email.split("@")[1]
    if domain in countedEmailDomains.keys():
        countedEmailDomains[domain] = countedEmailDomains[domain] + 1
    else:
        countedEmailDomains[domain] = 1

with open("task2/mail.json", "w") as f:
    json.dump(countedEmailDomains, f)

