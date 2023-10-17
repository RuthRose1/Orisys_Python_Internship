from lxml import html
import requests

response = requests.get('https://www.amazon.in/Sony-195229-Marvels-Spider-Man/dp/B07CR4GQD3?th=1')
content = response.content

tree = html.fromstring(content)

price = tree.xpath('//span[@class="a-price-whole"]')
for i in price:
    text_content = i.text_content()
    print(text_content)