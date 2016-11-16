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


def get_definitions_and_ratings(soup):
    defs_and_ratings = []
    for div in soup.find_all(class_='def-panel'):
        thumbs_div = div.find(class_='thumbs')
        try:
            defs_and_ratings.append({
                'meaning': div.find(class_='meaning').text.strip(),
                'thumbs_up': thumbs_div.find(class_='up').text.strip(),
                'thumbs_down': thumbs_div.find(class_='down').text.strip()
            })
        except AttributeError:
            pass

    return defs_and_ratings

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
