#!/usr/bin/env python3
from sys import argv
import feedbooks as fb
from books import Book

def create_objects(book_data_list):
    book_list = []
    for data in book_data_list:
        title           = data[0]
        author          = data[1]
        description     = data[2]
        cover_url       = data[3]
        download_url    = data[4]
        link            = data[5]
        source          = data[6]
        book_list.append(Book(title, author, 'No description', cover_url,
            download_url, link, source))
    return book_list

def download_file(book_to_download):
    book_to_download.download()
    return None

def present_results(book_list):
    for i, book in enumerate(book_list):
        print(str(i)+'.', "'"+book.title+"'", 'by', book.author)
    return None

if __name__ == '__main__':
    book_data_list = fb.fetch_results(argv[-1])
    book_list = create_objects(book_data_list)
    present_results(book_list)
    download_choice = input('Enter number of file to download\n> ')
    download_file(book_list[int(download_choice)])
    print('File finished downloading from %s' % book_list[int(download_choice)].source)
