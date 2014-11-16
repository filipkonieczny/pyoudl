#!/usr/bin/env python
# encoding: utf-8


# TODO: documentation
# description


# TODO: enable downloading Streamus playlists based on a json file
# TODO: add '*.mp3' metadata based on youtube's guess


# imports
import os
import sys

import requests
import dryscrape
from bs4 import BeautifulSoup


# constant variables
BASE_YOUTUBE_MP3_URL = 'http://www.youtube-mp3.org'
BASE_YOUTUBE_URL = 'http://www.youtube.com'

# TODO: windows directory path workaround
DEFAULT_DIRECTORY = 'music/'

# url types
PLAYLIST = 'playlist'
SONG = 'song'
JSON = 'json'
INVALID = 'invalid'

# TODO: format messages
HELLO = '\nHello!\n\n'
GOODBYE = '\n\nGoodbye!\n'
NO_URL_SUPPLIED = 'No url supplied!'
INVALID_URL = 'Invalid url!'
DOWNLOADING = "Downloading: '{}' {}."
DOWNLOAD_FINISHED = '{} {} download finished!\n'


# functions
def url_validation(url):
    # TODO: documentation
    '''
    '''

    if not isinstance(url, type('')):
        return False

    if 'youtu.be' in url or \
       'youtube.com' in url:
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

        # check if is a youtube song
        if '?v=' in url:
            return SONG

    # TODO: check if is a json file
    # return JSON

    return INVALID


def convert_playlist_to_dict(url):
    # TODO: documentation
    '''
    '''

    songs = {}
    songs_urls = []

    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    soup = BeautifulSoup(response)

    playlist_name = soup.find_all('meta')[0].get('content')
    songs['playlist_name'] = playlist_name
    for link in soup.find_all('a'):
        link = link.get('href')
        if '/watch?v=' in link:
            link = link.split('&list')[0]
            song_url = BASE_YOUTUBE_URL + link
            if song_url not in songs_urls:
                songs_urls.append(song_url)

    songs['songs_urls'] = songs_urls

    return songs


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
    destination_url = '{}/?c#v={}'.format(BASE_YOUTUBE_MP3_URL, song_id)
    session = dryscrape.Session()
    session.visit(destination_url)
    response = session.body()
    soup = BeautifulSoup(response)

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

    download_url = '{}{}'.format(BASE_YOUTUBE_MP3_URL, download_url)

    data = {
        'title': title,
        'download_url': download_url
    }

    return data


def download_song(download_data, directory=DEFAULT_DIRECTORY):
    # TODO: documentation
    '''
    '''

    title = download_data['title']
    download_url = download_data['download_url']

    print DOWNLOADING.format(title, SONG)

    # TODO: set '*.mp3' metadata - could be tricky?
    # TODO: check for duplicates
    r = requests.get(download_url, stream=True)
    with open('{}{}.mp3'.format(directory, title), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()

    print DOWNLOAD_FINISHED.format(title, SONG)


def get_single_song(url, directory=DEFAULT_DIRECTORY):
    # TODO: documentation
    '''
    '''

    download_data = get_download_data(url)
    download_song(download_data, directory=directory)


def get_multiple_songs(songs):
    # TODO: documentation
    '''
    '''

    playlist_name = songs['playlist_name']
    songs_urls = songs['songs_urls']

    # TODO: check if such directory already exists
    directory = DEFAULT_DIRECTORY + playlist_name + '/'
    os.makedirs(directory)

    print DOWNLOADING.format(playlist_name, PLAYLIST)

    # TODO: add a counter, like "song 1/12"
    for song_url in songs_urls:
        get_single_song(song_url, directory=directory)

    print DOWNLOAD_FINISHED.format(playlist_name, SONG)


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

        # if system argument is an url to a song
        if url_type == SONG:
            get_single_song(url)
            continue

        # if system argument is an url to a playlist
        if url_type == PLAYLIST:
            songs = convert_playlist_to_dict(url)
        # if system argument is a json file
        else:
            songs = convert_json_to_list()

        get_multiple_songs(songs)


def main(system_arguments):
    # TODO: documentation
    '''
    '''

    # TODO: statistics - measure the time it took to download,
    # files count, size, anything you can get a hold of.

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
