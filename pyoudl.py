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
BASE_URL = 'http://www.youtube-mp3.org'

PLAYLIST = 'playlist'
VIDEO = 'video'
JSON = 'json'
INVALID = 'invalid'

HELLO = '\nHello!\n\n'
GOODBYE = '\n\nGoodbye!\n'
NO_URL_SUPPLIED = 'No url supplied!'
INVALID_URL = 'Invalid url!'
DOWNLOADING = "Downloading: '{}'"
DOWNLOAD_FINISHED = 'Download finished!\n'


# functions
def url_validation(url):
    # TODO: documentation
    '''
    '''

    if not isinstance(url, type('')):
        return False

    if 'http://youtu.be' in url or \
       'https://www.youtube.com' in url:
        return True

    return False


def get_url_type(url):
    # TODO: documentation
    '''
    '''

    # check if is a youtube link
    if url_validation(url):
        # check if is a youtube playlist
        if 'list=' in url:
            return PLAYLIST

        # check if is a youtube video
        if '?v=' in url:
            return VIDEO

    # TODO: check if is a json file
    # return JSON

    return INVALID


def convert_playlist_to_list():
    # TODO: documentation
    '''
    '''

    pass


def convert_json_to_list():
    # TODO: documentation
    '''
    '''

    # TODO: validate every link with url_validation()
    pass


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

    print DOWNLOADING.format(title), 'video.'

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


def get_multiple_songs(songs_urls):
    # TODO: documentation
    '''
    '''

    # TODO: add a counter, like "song 1/12"

    for song_url in songs_urls:
        get_single_song(song_url)


def get_music(system_arguments):
    # TODO: documentation
    '''
    '''

    # iterate through every system argument
    for url in system_arguments:
        # check if system argument is a valid url
        url_type = get_url_type(url)
        if url_type == INVALID:
            print INVALID_URL
            return

        # if system argument is an url to a video
        if url_type == VIDEO:
            get_single_song(url)
            continue

        # if system argument is an url to a playlist
        if url_type == PLAYLIST:
            songs_urls = convert_playlist_to_list()
        # if system argument is a json file
        else:
            songs_urls = convert_json_to_list()

        get_multiple_songs(songs_urls)


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

    get_music(system_arguments[1:])

    print GOODBYE


# run main function
if __name__ == "__main__":
    main(sys.argv)
