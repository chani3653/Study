#indeed
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})# 페이지 넘버 부분 html을 가져온다
  links = pagination.find_all('a')#모든 링크를 찾아 준다
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
  for result in results:
    title = result.find("div",{"class":"title"}).find("a")["title"]
    print(title)
  return jobs