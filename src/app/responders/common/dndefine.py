"""
Definition webhook responder
"""
import logging
import urllib2

from app.responders.slack import SlackResponder
from settings import DNDFINE_TOKENS


class DndefineResponder(object):
    """ Define a word! """
    KEY_WORD = 'dndfine'
    TOKENS = DNDFINE_TOKENS

    def get_definitions(self, term):
        logging.info('Searching checking dict for term: %s', term)

        return self._format_response(term, DEFINITIONS.get(term.lower()))

    @staticmethod
    def _format_response(term, definition):
        response = ''

        response += '*{}*\n\n'.format(term)

        if definition:
            response += '\n\n' + definition + '\n'
        else:
            response += 'There aren\'t any definitions for {} yet.'.format(term)

        return response

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))


class DndefineSlackResponder(DndefineResponder, SlackResponder):
    """
    Responds to /udefine/slack/ requests
    """


DEFINITIONS = {
    'initiative': 'Roll 1d20 + dex modifier'
}