import bs4
import requests
import csv
import json


#reads and saves txt file to variable named 'file'
text = open('100QueriesSet2.txt', mode='r')


#for loop that iterates over each keyword in the text file
for keyword in text:
    url = 'https://www.search.yahoo.com/search?p='+keyword+'&num='+str(30)
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    a_link = soup.find('ol', class_='reg searchCenterMiddle').a['href']

    #print(keyword, a_link)
    print(keyword, a_link)
