from webapp2 import RequestHandler
from webapp2_extras import json



class BootstrapResponder(RequestHandler):
    """
    Inflates datastore with the data from http://www.dnd5eapi.co/.
    """

    URL_TEMPLATE = "http://www.dnd5eapi.co"

    SUPPORTED


    def get(self):
        """
        Receive the get!
        """
        self.request.get('type')
        self.response.write('done')


    @classmethod
    def check_credentials(cls, token):
        return True
