#!/usr/bin/env python3
from sys import argv
import requests
import urllib.request
from bs4 import BeautifulSoup

class Book:
    def __init__(self, title, author, description, cover_url, download_url, link):
        self.title          = title
        self.author         = author
        self.description    = description
        self.cover_url      = cover_url
        self.download_url   = download_url
        self.link           = link
        
    def __str__(self):
        return "{:<17}{:<17}{:<50}{:<20}{:<20}{:<20}".format(
                self.title, self.author, self.description, self.cover_url, 
                self.download_url, self.link)

    def download(self):
        urllib.request.urlretrieve(self.download_url, self.title+'.epub')
        return None



def fetch_results(search_query):
    base_url = "http://www.feedbooks.com/books/search?query="

    r = requests.get(base_url+search_query)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text)
        
        book_list = []
        for entry in soup('div', {'itemtype' : 'http://schema.org/Book'}):
            title = entry('a', {'itemprop' : 'url'})[0]
            title = title.string

            author = entry('a', {'class' : 'gray'})[0]
            author = author.string
            
            # note done
            #description = entry('div', {'class' : 'span-11 prepend-1 append-bottom'})
            #description = description[0].text
            #print(description)

            cover_url = entry('img', {'class' : 'cover medium-cover'})[0]
            cover_url = cover_url.get('src')

            download_url = entry('a', {'title' : 'Download in EPUB'})[0]
            download_url = download_url.get('href')

            link = entry('a')[0]
            link = link.get('href')

            book_list.append(Book(title, author, 'No description', cover_url,
                download_url, link))

    else:
        print('Error:', r.status_code)
        return None
    return book_list


def download_file():
    return None

def present_results():
    return None

if __name__ == '__main__':
    book_list = fetch_results(argv[-1])
