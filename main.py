import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=84a541c104b5b24c")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

# print(pagination)

pages = pagination.find_all('a')
# print(pages)

spans = []

for page in pages:
    spans.append(page.find("span"))


print(spans[0:-1])
