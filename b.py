
#libraries used
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def scrape(q):
    html_page = urlopen("https://www.search.yahoo.com/search?p="+q)
    soup = BeautifulSoup(html_page, "lxml")
    #stores links in a list
    links = []
    for link in soup.findAll("a", class_="d-ib ls-05 fz-20 lh-26 td-hu tc va-bot mxw-100p"):
        links.append(link.get("href"))
        
        print(q, links)

file = open('100QueriesSet2.txt')
for query in file.readlines():
    q = query



# execute function
scrape(q)