# indeed 웹사이트 python페이지 Web Scrapping
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  # requests로 url페이지 가져오기
  result = requests.get(URL)

  # bs4로 html 데이터 탐색
  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []

  for link in links[:-1]:
    pages.append(int(link.string)) # 페이지 수를 int로 변환

  max_page = pages[-1] # 가장 마지막 페이지
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  
  for result in results:
    title = result.find("h2", {"class":"title"}).find("a")["title"]
    print(title) # indeed 웹페이지 title scrapping
  return jobs
