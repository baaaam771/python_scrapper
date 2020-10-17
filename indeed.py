import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

    # for n in range(max_page):
    #  print(f"start={n*50}")


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    # find_all 은 리스트의 모든 부분
    # find는 찾은 곳의 첫 부분
    # print(results)
    for result in results:
        # title = (result.find("h2", {"class": "title"}))
        # anchor = title.find("a")["title"]
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        print(title)
        company = result.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            # print(str(company.find("a").string))
            company = str(company.find("a").string)
        else:
            # print(str(company.string).strip())
            company = str(company.string)
        company = company.strip()
        print(title, company)
    return jobs
