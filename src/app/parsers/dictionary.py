"""
dictionary.com parsers
"""
from bs4 import BeautifulSoup


def get_definitions(soupable_html, definitions_class):
    soup = BeautifulSoup(soupable_html, 'lxml')
    # Work some magic.
    meanings = [definition_content.text.replace('\n', '') for definition_content
                in soup.find_all(class_=definitions_class)]

    return meanings
