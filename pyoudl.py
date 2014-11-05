#!/usr/bin/env python
# encoding: utf-8


# TODO: documentation
# description


# imports
import requests
import sys


# TODO: format messages
# constant variables
HELLO = '\nHello!\n\n'
GOODBYE = '\n\nGoodbye!\n'
NO_LINK_SUPPLIED = 'No link supplied!'
INVALID_LINK = 'Invalid link!'


# functions
def link_validation(link):
    # TODO: documentation
    '''
    '''

    return True


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


def get_music(link):
    # TODO: documentation
    '''
    '''

    pass


def main(system_arguments):
    # TODO: documentation
    '''
    '''

    system_arguments_length = len(system_arguments)

    print HELLO

    # check if any system arguments were supplied
    if system_arguments_length == 1:
        print NO_LINK_SUPPLIED
        return

    # iterate through every system argument
    for i in xrange(1, system_arguments_length):
        link = system_arguments[i]

        # check if system argument is a valid link
        if link_validation(link):
            print 'Link valid! {}'.format(link)
            get_music(link)
        else:
            print INVALID_LINK
            return

    print GOODBYE


# run main function
if __name__ == "__main__":
    main(sys.argv)
