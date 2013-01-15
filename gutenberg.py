#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def fetch_results(search_query):
    base_url = "http://www.gutenberg.org/ebooks/search/?query="
    
    # format query from "The Great Gatsby" to "The+Great+Gatsby"
    search_query = search_query.split()
    search_query = '+'.join(search_query)
    
    user_agent = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17'}

    r = requests.get(base_url+search_query, headers = user_agent)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text)
        
        book_data_list = []
        for entry in soup('li', {'class' : 'booklink'}):
            if not 'icon_audiobook' in str(entry):
                title = entry('span', {'class' : 'title'})[0]
                title = title.string
                try:
                    author = entry('span', {'class' : 'subtitle'})[0]
                    author = author.string
                except:
                    author = 'No author'
                # not done
                #description = entry('div', {'class' : 'span-11 prepend-1 append-bottom'})
                #description = description[0].text
                #print(description)
                try:
                    cover_url = entry('img', {'class' : 'cover-thumb'})[0]
                    cover_url = cover_url.get('src')
                except:
                    cover_url = 'No cover'
                link = entry('a', {'class' : 'link'})[0]
                link = 'http://www.gutenberg.org' + link.get('href')
                download_url = link + '.epub'
                source = 'Gutenberg.org'

                book_data_list.append([title, author, 'No description', cover_url,
                    download_url, link, source])
            else:
                None
    else:
        print('Error:', r.status_code)
        return None
    return book_data_list
