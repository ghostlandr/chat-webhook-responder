"""
Definition webhook responder
"""
import logging
import urllib2

from settings import DEFINE_TOKENS
from app.parsers.dictionary import get_definitions


class DefineResponder(object):
    """ Define a word! """
    DICTIONARY_URI_TEMPLATE = 'http://dictionary.reference.com/browse/{}'
    DICTIONARY_DOT_COM_DEFINITIONS_CLASS = 'def-content'
    KEY_WORD = 'define'
    PLATFORM = ''  # Override in child class

    def get_definitions(self, term):
        if ' ' in term:
            # Won't work so hot at this time, return an error
            return 'Only single words are supported right now.'

        logging.info('Searching dictionary.com for term: %s', term)

        try:
            result = urllib2.urlopen(self.DICTIONARY_URI_TEMPLATE.format(term))
            definitions = get_definitions(result, self.DICTIONARY_DOT_COM_DEFINITIONS_CLASS)

            return self._format_response(term, definitions)
        except urllib2.URLError as ue:
            if ue.code == 404:
                return 'Can\'t find anything for *{}*!'.format(term)
            # We don't know (read: haven't implemented) what went wrong, return something generic.
            return 'Something went wrong with the request.'

    @staticmethod
    def _format_response(term, definitions):
        response = ''

        if len(definitions) > 5:
            response += 'Oh boy, there are a lot of definitions for this one! Here are the first five.\n'
        else:
            response += 'Here we are:\n'

        response += '*{}*\n\n'.format(term.capitalize())

        # Format like '1. Definition text'.
        response += '\n'.join([unicode(index + 1) + u'. ' + definition.capitalize().strip()
                               for index, definition in enumerate(definitions[:5])])

        return response

    @classmethod
    def check_credentials(cls, token):
        return token in DEFINE_TOKENS[cls.PLATFORM]

    def process(self, args):
        term = ' '.join(self.prepare_string(args).split(' ')[1:]).strip()

        return self.get_definitions(term)
