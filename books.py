#!/usr/bin/env python3
import urllib.request

class Book:
    def __init__(self, title, author, description, cover_url, download_url, link,
            source):
        self.title          = title
        self.author         = author
        self.description    = description
        self.cover_url      = cover_url
        self.download_url   = download_url
        self.link           = link
        self.source         = source
        
    def __str__(self):
        return "{:<17}{:<17}{:<50}{:<20}{:<20}{:<20}{:<20}".format(
                self.title, self.author, self.description, self.cover_url, 
                self.download_url, self.link, self.source)

    def download(self):
        urllib.request.urlretrieve(self.download_url, self.title+'.epub')
        return None
