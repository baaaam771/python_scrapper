import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=84a541c104b5b24c")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

# print(pagination)

links = pagination.find_all('a')
# print(pages)

pages = []

for link in links[:-1]:
    pages.append(int(link.string))
    # link.find("span").string=link.string
# pages = pages[0:-1]
max_page = pages[-1]
