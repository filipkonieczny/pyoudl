#!/usr/bin/env python
# encoding: utf-8


# TODO: documentation
# description


# imports
import sys

import requests
import dryscrape
from bs4 import BeautifulSoup


# constant variables
# TODO: format messages
HELLO = '\nHello!\n\n'
GOODBYE = '\n\nGoodbye!\n'
NO_URL_SUPPLIED = 'No url supplied!'
INVALID_URL = 'Invalid url!'
BASE_URL = 'http://www.youtube-mp3.org'


# functions
def url_validation(url):
    # TODO: documentation
    '''
    '''

    # TODO: url_validation
    return True


def get_download_url(url):
    # TODO: documentation
    '''
    '''

    # TODO: add information for user to know what's going on

    song_id = url.split('?v=')[-1]

    # TODO: documentation
    destination_url = '{}/?c#v={}'.format(BASE_URL, song_id)
    session = dryscrape.Session()
    session.visit(destination_url)
    response = session.body()
    soup = BeautifulSoup(response)

    # TODO: remove saving log file
    data = str(soup)
    f = open('log.html', 'w')
    f.write(data)
    f.close()

    # TODO: documentation
    download_url = ''
    for link in soup.find_all('a'):
        link = link.get('href')
        if '/get?ab=' in link:
            download_url = link
            break

    download_url = '{}{}'.format(BASE_URL, download_url)

    return download_url


def download_song(download_url):
    # TODO: documentation
    '''
    '''

    # TODO: add information for user to know what's going on

    # HARDCODED FOR TESTING PURPOSES
    # TODO: crawl song name
    song_name = 'david guetta - dangerous ft. sam martin'
    song_name = 'foo'

    # TODO: set '*.mp3' metadata
    # TODO: check for duplicates
    r = requests.get(download_url, stream=True)
    with open('{}.mp3'.format(song_name), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()


def get_single_song(url):
    # TODO: documentation
    '''
    '''

    download_url = get_download_url(url)
    download_song(download_url)


def get_multiple_songs():
    # TODO: documentation
    '''
    '''

    pass


def get_music(url):
    # TODO: documentation
    '''
    '''

    # TODO: determine if it's a playlist
    get_single_song(url)


def main(system_arguments):
    # TODO: documentation
    '''
    '''

    system_arguments_length = len(system_arguments)

    print HELLO

    # check if any system arguments were supplied
    if system_arguments_length == 1:
        print NO_URL_SUPPLIED
        return

    # iterate through every system argument
    for i in xrange(1, system_arguments_length):
        url = system_arguments[i]

        # check if system argument is a valid url
        if url_validation(url):
            get_music(url)
        else:
            print INVALID_URL

    print GOODBYE


# run main function
if __name__ == "__main__":
    main(sys.argv)
