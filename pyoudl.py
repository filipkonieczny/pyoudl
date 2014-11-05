#!/usr/bin/env python
# encoding: utf-8


# TODO: documentation
# description


# imports
import requests
import sys
from bs4 import BeautifulSoup


# TODO: format messages
# constant variables
HELLO = '\nHello!\n\n'
GOODBYE = '\n\nGoodbye!\n'
NO_URL_SUPPLIED = 'No url supplied!'
INVALID_URL = 'Invalid url!'


# functions
def url_validation(url):
    # TODO: documentation
    '''
    '''

    return True


def get_download_url(url):
    # TODO: documentation
    '''
    '''

    # HARDCODED FOR TESTING PURPOSES
    url = 'http://www.youtube.com/watch?v=FsfrsLxt0l8'

    # HARDCODED FOR TESTING PURPOSES
    song_id = url  # TODO: determine song_id based on url
    song_id = 'FsfrsLxt0l8'

    # url to go to
    destination_url = 'http://www.youtube-mp3.org/?c#v={}'.format(song_id)

    # crawl information from destination url
    r = requests.get(destination_url)
    soup = BeautifulSoup(r.content)
    print soup.prettify()  # TODO: convince youtube-mp3.org that JS is enabled

    return


def download_song(url):
    # TODO: documentation
    '''
    '''

    # HARDCODED FOR TESTING PURPOSES
    song_name = 'david guetta - dangerous ft. sam martin'
    download_url = get_download_url(url)
    download_url = 'http://www.youtube-mp3.org/get?ab=128&video_id=FsfrsLxt0l8&h=8cb6d623bcf4fc8957bc7b9174bd33db&r=1415214691386.1618413236&s=115694'

    r = requests.get(download_url, stream=True)
    with open('{}.mp3'.format(song_name), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()


def get_single_song():
    # TODO: documentation
    '''
    '''

    pass


def get_multiple_songs():
    # TODO: documentation
    '''
    '''

    pass


def get_music(url):
    # TODO: documentation
    '''
    '''

    download_song(url)


def main(system_arguments):
    # TODO: documentation
    '''
    '''

    # HARDCODED FOR TESTING PURPOSES
    system_arguments = ('pyoudl.py', 'http://www.youtube.com/watch?v=FsfrsLxt0l8')

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
            return

    print GOODBYE


# run main function
if __name__ == "__main__":
    main(sys.argv)
