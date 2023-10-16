from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
content = response.content #Content of reponse
soup = BeautifulSoup(content, "html.parser")

#Headings along with numbers
print('\n Heading and number: ')
element = soup.find_all(class_= 'title')
for i in element:
    element_txt = i.text
    print(element_txt)
    
#Only headings
print('\nOnly Heading: ')
headings = soup.find_all(class_='titleline')
for i in headings:
    headings_txt = i.text
    print(headings_txt)
    
    
#Score
print('\n')
print('Point: ')
point = soup.find_all(class_='score')
for i in point:
    point_txt = i.text
    print(point_txt)
    
    
#Links
print('\n')
print('Link: ')
link = soup.find_all(class_ = "titleline")
for i in link:
    print(i.a.get("href"))