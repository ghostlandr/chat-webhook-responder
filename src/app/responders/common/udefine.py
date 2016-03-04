"""
Definition webhook responder
"""
import logging
import urllib2

from app.parsers.dictionary import get_definitions


class UDefineResponder(object):
    """ Define a word! """
    URBAN_DICTIONARY_TEMPLATE = 'http://www.urbandictionary.com/define.php?term={}'
    URBAN_DICTIONARY_DOT_COM_DEFINITIONS_CLASS = 'meaning'
    KEY_WORD = 'define'

    def get_definitions(self, term):
        logging.info('Searching urbandictionary.com for term: %s', term)

        try:
            result = urllib2.urlopen(self.URBAN_DICTIONARY_TEMPLATE.format(term))
            definitions = get_definitions(result, self.URBAN_DICTIONARY_DOT_COM_DEFINITIONS_CLASS)

            return self._format_response(term, definitions)
        except urllib2.URLError as ue:
            if ue.code == 404:
                return 'Can\'t find anything for *{}*!'.format(term)
            # We don't know (read: haven't implemented) what went wrong, return something generic.
            return 'Something went wrong with the request.'

    @staticmethod
    def _format_response(term, definitions):
        response = ''

        response += '*{}*\n\n'.format(term)

        response += '\n\n'.join(definition for definition in definitions[:5])

        return response