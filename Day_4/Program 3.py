from bs4 import BeautifulSoup

file = open("Program 1.html")
content = file.read()
file.close()
#print(content)

soup = BeautifulSoup(content, "html.parser") #html.parser -> used for web scraping; html.parser won't work in all cases so we need to use lxml

'''
print(soup)
print(soup.prettify())''' #For alignment


'''
print(soup.title)#soup is the soup title
print(soup.a)#only first a is printed
print(soup.h1)
'''
'''
print(soup.find_all(name = 'a'))''' #To find all a

print(soup.h1.text) #first heading text only.

print(soup.find(name = "a").getText())

print('\n')
print(soup.find(name = 'a').get('href')) #Link of 1st link

print('\n')
all_links = soup.find_all(name = 'a')
for link in all_links:
    print(link.getText())
    print(link.get('href'))
    
print('\n')
print(soup.find(name="h1", id="first_heading").getText()) #first heading using id

print('\n')
first_heading = soup.find(class_ = "small-para") #class is keyword. so use _ for this purpose
print(first_heading.getText())

print('\n')
first_heading = soup.select(selector = "div .headings") #selector
for i in first_heading:
    print(i.getText())

print('\n')
#if this returns 2 headings, we need a specific one. use id or
first_heading = soup.select(selector = "#last_heading") #selector
for i in first_heading:
    print(i.getText())

print('\n')
first_heading = soup.select(selector = ".last_heading .headings")
for i in first_heading:
    print(i.getText())