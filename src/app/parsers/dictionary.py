"""
dictionary.com parsers
"""
from bs4 import BeautifulSoup


def get_soup(soupable_html):
    return BeautifulSoup(soupable_html, 'lxml')


def get_definitions(soup, definitions_class):
    # Work some magic.
    meanings = [definition_content.text.replace('\n', '') for definition_content
                in soup.find_all(class_=definitions_class)]

    return meanings


def get_difficulty_index(soup):
    try:
        return soup.find(id='difficulty-box').find(class_='subtext').contents[0]
    except AttributeError:
        # This page doesn't have a difficulty-box on it
        return ''


def get_word_type(soup):
    try:
        types = soup.find(class_='def-list').find(class_='luna-data-header')
        return types.text.strip()  # Leaving this on its own line for possible future enhancements
    except AttributeError:
        return ''
