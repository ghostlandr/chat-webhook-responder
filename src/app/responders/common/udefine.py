"""
Definition webhook responder
"""
import logging
import unicodedata
import urllib2

from app.parsers.dictionary import get_soup, get_definitions_and_ratings
from app.responders.slack import SlackResponder
from settings import UDEFINE_TOKENS


class UDefineResponder(object):
    """ Define a word! """
    URBAN_DICTIONARY_TEMPLATE = 'http://www.urbandictionary.com/define.php?term={}'
    URBAN_DICTIONARY_DOT_COM_DEFINITIONS_CLASS = 'meaning'
    KEY_WORD = 'define'
    TOKENS = UDEFINE_TOKENS

    def get_definitions(self, term):
        logging.info('Searching urbandictionary.com for term: %s', term)

        try:
            safe_term = unicodedata.normalize('NFKD', term).encode('ascii', 'ignore')

            result = urllib2.urlopen(self.URBAN_DICTIONARY_TEMPLATE.format(urllib2.quote(safe_term)))
            definitions = get_definitions_and_ratings(get_soup(result))

            return self._format_response(term, definitions)
        except urllib2.URLError as ue:
            if ue.code == 404:
                return u'Can\'t find anything for *{}*!'.format(term)
            elif str(ue.code).startswith('4'):
                logging.info(u'Got an error: {}, trying again'.format(ue.message))
                return self.get_definitions(term)
            # We don't know (read: haven't implemented) what went wrong, return something generic.
            return 'Something went wrong with the request.'

    @staticmethod
    def _format_response(term, definitions):
        response = u''

        response += u'*{}*\n\n'.format(term)

        if len(definitions) > 0:
            response += '\n\n'.join(u'{}\n:+1: {} :-1: {}'.format(
                definition['meaning'],
                definition['thumbs_up'],
                definition['thumbs_down']
            ) for definition in definitions[:5])
        else:
            response += u'There aren\'t any definitions for {} yet. Can you define it?'.format(term)

        return response

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))


class UDefineSlackResponder(UDefineResponder, SlackResponder):
    """
    Responds to /udefine/slack/ requests
    """
