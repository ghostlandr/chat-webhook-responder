"""
Definition webhook responder
"""
import logging
import urllib2

from app.responders import BaseResponder

from app.parsers.dictionary import get_definitions
from settings import DEFINE_TOKENS


class DefineResponder(BaseResponder):
    """ Define a word! """
    DICTIONARY_TEMPLATE = 'http://dictionary.reference.com/browse/{}'

    @staticmethod
    def check_credentials(token):
        return token in DEFINE_TOKENS

    def process(self, text, trigger_word):
        term = text.split(':')[1].strip()

        logging.info('Going to town on: %s', term)

        if ' ' in term:
            # Won't work so hot at this time, return an error
            return 'Only single words are supported right now. :bow:'

        logging.info('Searching dictionary.com for term: %s', term)

        try:
            result = urllib2.urlopen(self.DICTIONARY_TEMPLATE.format(term))
            definitions = get_definitions(result)

            return self._format_response(term, definitions)
        except urllib2.URLError as ue:
            if ue.code == 404:
                return 'Can\'t find anything for *{}*! :bow:'.format(term)
            # We don't know (read: haven't implemented) what went wrong, return something generic.
            return 'Something went wrong with the request. :bow:'

    @staticmethod
    def _format_response(term, definitions):
        response = ''

        if len(definitions) > 5:
            response += 'Oh boy, there are a lot of definitions for this one! Here are the first five.\n'
        else:
            response += 'Here we are:\n'

        response += '*{}*\n\n'.format(term.capitalize())

        # Format like '1. Definition text'.
        response += '\n'.join([str(index + 1) + '. ' + definition.capitalize()
                               for index, definition in enumerate(definitions[:5])])

        return response


