"""
dictionary.com parsers
"""
import logging

from bs4 import BeautifulSoup


def get_definitions(result):
    soup = BeautifulSoup(result, 'lxml')
    # Work some magic.
    return [text.text.replace('\n', '') for text in soup.find_all(class_='def-content')]
