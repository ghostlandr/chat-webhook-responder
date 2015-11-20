"""
dictionary.com parsers
"""
from bs4 import BeautifulSoup


def get_definitions(result):
    soup = BeautifulSoup(result, 'lxml')
    # Work some magic.
    meanings = [definition_content.text.replace('\n', '') for definition_content in soup.find_all(class_='meaning')]
    # examples = [definition_content.text.replace('\n', '') for definition_content in soup.find_all(class_='example')]

    return meanings
