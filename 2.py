import json
from urllib.parse import urljoin
import requests
from parsel import Selector

index = requests.get('http://books.toscrape.com/')
books = []

for href in Selector(index.text).css('.product_pod a::attr(href)').extract():
    url = urljoin(index.url, href)
    book_page = requests.get(url)
    sel = Selector(book_page.text)
    books.append({
        'title': sel.css('h1::text').extract_first(),
        'price': sel.css('.product_main .price_color::text')extract_first(),
        'image': sel.css('#product_gallery img::attr(src)').extract_first()
    })

with open('books.json', 'w') as fp:
    json.dump(books, fp)
