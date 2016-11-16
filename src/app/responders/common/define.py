"""
Definition webhook responder
"""
import logging
import urllib2

from app.responders.hipchat import HipChatResponderMixin
from app.responders.slack import SlackResponder
from settings import DEFINE_TOKENS
from app.parsers.dictionary import get_definitions, get_soup, get_difficulty_index, get_word_type


class NoDefinitionFoundError(Exception):
    def __init__(self):
        self.code = 404


class DefineResponder(object):
    """ Define a word! """
    DICTIONARY_URI_TEMPLATE = 'http://dictionary.reference.com/browse/{}'
    DICTIONARY_DOT_COM_DEFINITIONS_CLASS = 'def-content'
    KEY_WORD = 'define'
    TOKENS = DEFINE_TOKENS

    def get_definitions(self, term):
        # if ' ' in term:
        #     Won't work so hot at this time, return an error
            # return 'Only single words are supported right now.'

        logging.info('Searching dictionary.com for term: %s', term)

        try:
            result = urllib2.urlopen(self.DICTIONARY_URI_TEMPLATE.format(urllib2.quote(term)))
            dat_soup = get_soup(result)
            definitions = get_definitions(dat_soup, self.DICTIONARY_DOT_COM_DEFINITIONS_CLASS)
            if not definitions:
                raise NoDefinitionFoundError
            word_difficulty = get_difficulty_index(dat_soup)
            word_type = get_word_type(dat_soup)

            return self._format_response(term, definitions, word_difficulty, word_type)
        except (NoDefinitionFoundError, urllib2.URLError) as ue:
            if ue.code == 404:
                return 'Can\'t find anything for *{}*!'.format(term)
            # We don't know (read: haven't implemented) what went wrong, return something generic.
            return 'Something went wrong with the request.'

    @staticmethod
    def _format_response(term, definitions, word_difficulty, word_type='verb'):
        response = ''

        word_difficulty = '({})'.format(word_difficulty) if word_difficulty else ''
        word_type = '_{}_\n'.format(word_type) if word_type else ''
        response += '*{}* {}\n{}\n'.format(term.capitalize(), word_difficulty, word_type)

        # Format like '1. Definition text'.
        response += '\n'.join([unicode(index + 1) + u'. ' + definition.capitalize().strip()
                               for index, definition in enumerate(definitions[:5])])

        return response

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))


class DefineSlackResponder(DefineResponder, SlackResponder):
    """
    Responds to Slack define requests
    """


class DefineHipChatResponder(DefineResponder, HipChatResponderMixin):
    PLATFORM = 'hipchat'

    def process(self, args):
        term = self.prepare_string(args)[len(self.KEY_WORD):].strip()

        return self.get_definitions(term)
