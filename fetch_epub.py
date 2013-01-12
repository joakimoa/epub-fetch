#usr/bin/python3
from sys import argv
import requests
import urllib.request

class Book:
    def __init__(self, title, author, description, cover_url, download_url, link):
        self.title          = title
        self.author         = author
        self.description    = description
        self.cover_url      = cover_url
        self.download_url   = download_url
        self.link           = link
        
    def __str__(self):
        return "{:<17}{:<4}{:<4}{:<7}{:<13}{:<15}".format(
                self.title, self.author, self.description, self.cover_url, 
                self.download_url, self.link)

    def download(self):
        return None



def fetch_results(search_query):
    base_url = "http://www.feedbooks.com/books/search?query="

    r = requests.get(base_url+search_query)
    if r.status_code == requests.codes.ok:
        print()
    else:
        print('Error:', r.status_code)
    


    print(search_query)
    return None

def download_file():
    return None

def present_results():
    return None

if __name__ == '__main__':
    fetch_results(argv[-1])
