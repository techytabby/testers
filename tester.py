from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import json



# query_yahoosearch() reads .txt query file line by line, uses yahoo search engine to search query,and returns two lists keywords and url sear

file = open('100QueriesSet2.txt', mode='r')
y_links=[]
keyword = []
#for loop that iterates over each keyword in the text file
for keyword in file:
    url = 'https://www.search.yahoo.com/search?p='+keyword+'&num='+str(30)
    request_result = requests.get(url)
    soup = BeautifulSoup(request_result.text, "html.parser")
    y_links = [a['href'] for a in soup.find_all('a',class_="d-ib ls-05 fz-20 lh-26 td-hu tc va-bot mxw-100p", href=True)]
    #print(keyword, y_links)
    print(keyword, y_links)