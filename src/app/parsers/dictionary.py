"""
dictionary.com parsers
"""
import logging

from bs4 import BeautifulSoup


def get_definitions(result):
    soup = BeautifulSoup(result, 'lxml')
    # Work some magic.
    return [definition_content.text.replace('\n', '') for definition_content in soup.find_all(class_='def-content')]
