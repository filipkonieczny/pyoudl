#!/usr/bin/env python
# encoding: utf-8


# TODO: documentation
# description


# TODO: enable downloading Streamus playlists based on a json file
# TODO: add '*.mp3' metadata based on youtube's guess


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
DOWNLOADING = "Downloading: '{}'"
DOWNLOAD_FINISHED = 'Download finished!\n'
BASE_URL = 'http://www.youtube-mp3.org'


# functions
def url_validation(url):
    # TODO: documentation
    '''
    '''

    if 'http://youtu.be' in url or \
       'https://www.youtube.com' in url:
       return True

    return False


def get_download_data(url):
    # TODO: documentation
    '''
    '''

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

    # scrape song title
    title_data = str(soup.find(id='title'))
    title_data = title_data.split('</')[-2]
    title = title_data[3:]

    # TODO: documentation
    # scrape download url
    download_url = ''
    for link in soup.find_all('a'):
        link = link.get('href')
        if '/get?ab=' in link:
            download_url = link
            break

    download_url = '{}{}'.format(BASE_URL, download_url)

    data = {
        'title': title,
        'download_url': download_url
    }

    return data


def download_song(download_data):
    # TODO: documentation
    '''
    '''

    title = download_data['title']
    download_url = download_data['download_url']

    print DOWNLOADING.format(title)

    # TODO: set '*.mp3' metadata - could be tricky?
    # TODO: check for duplicates
    r = requests.get(download_url, stream=True)
    with open('{}.mp3'.format(title), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()

    print DOWNLOAD_FINISHED


def get_single_song(url):
    # TODO: documentation
    '''
    '''

    download_data = get_download_data(url)
    download_song(download_data)


def get_multiple_songs():
    # TODO: documentation
    '''
    '''

    # TODO: add a counter, like "song 1/12"
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
