#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def fetch_results(search_query):
    base_url = "http://www.feedbooks.com/books/search?query="
    
    # format query from "The Great Gatsby" to "The+Great+Gatsby"
    search_query = search_query.split()
    search_query = '+'.join(search_query)

    r = requests.get(base_url+search_query)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text)
        
        book_data_list = []
        for entry in soup('div', {'itemtype' : 'http://schema.org/Book'}):
            title = entry('a', {'itemprop' : 'url'})[0]
            title = title.string
            author = entry('a', {'class' : 'gray'})[0]
            author = author.string
            # not done
            #description = entry('div', {'class' : 'span-11 prepend-1 append-bottom'})
            #description = description[0].text
            #print(description)
            cover_url = entry('img', {'class' : 'cover medium-cover'})[0]
            cover_url = cover_url.get('src')
            download_url = entry('a', {'title' : 'Download in EPUB'})[0]
            download_url = download_url.get('href')
            link = entry('a')[0]
            link = link.get('href')
            source = 'Feedbooks.com'

            book_data_list.append([title, author, 'No description', cover_url,
                download_url, link, source])
    else:
        print('Error:', r.status_code)
        return None
    return book_data_list

