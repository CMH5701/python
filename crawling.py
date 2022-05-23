import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.daum.net"
#requests.get(url) 
response = requests.get(url)
#print(response.text[:500])

#print(type(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
#print(soup.title)#타이틀이 뭔지 출력
#print(soup.title.string)#타이틀 문자만 출력함
#soup.findAll("a","link_favorsch"))
results = soup.findAll('a','link_favorsch')
for result in results:
     print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
#print(response.url)

#print(response.content)

#print(response.encoding)

#print(response.headers)

#print(response.json)

#print(response.links)

#print(response.ok)

#print(response.status_code)