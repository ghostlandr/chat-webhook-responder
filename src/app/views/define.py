"""
Definition webhook responder
"""
import json
import logging
import urllib2

from webapp2 import RequestHandler

from app.parsers.dictionary import get_definitions


class DefineView(RequestHandler):
    """ Define a word! """
    DICTIONARY_TEMPLATE = 'http://dictionary.reference.com/browse/{}'

    def post(self):
        token = self.request.POST['token']
        text = self.request.POST.get('text')

        if token == '70XqnEL12zOlA08Fo0lraciE':
            # It's us!
            term = text.split(':')[1].strip()

            logging.info('Going to town on: %s', term)

            if ' ' in term:
                # Won't work so hot at this time, return an error
                return self.response.write(json.dumps({
                    'text': 'Only single words are supported right now. :bow:'
                }))

            logging.info('Searching dictionary.com for term: %s', term)

            try:
                result = urllib2.urlopen(self.DICTIONARY_TEMPLATE.format(term))
                definitions = get_definitions(result)

                return self.response.write(json.dumps({
                    'text': self._format_response(term, definitions)
                }))
            except urllib2.URLError as ue:
                if ue.code == 404:
                    return self.response.write(json.dumps({
                        'text': 'Can\'t find anything for *{}*! :bow:'.format(term)
                    }))
                return self.response.write(json.dumps({
                    'text': 'Something went wrong with the request. :bow:'
                }))

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


