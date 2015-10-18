"""
__init__.py
"""
from webapp2 import RequestHandler


class BaseResponder(RequestHandler):

    def check_credentials(self, token):
        return token == '70XqnEL12zOlA08Fo0lraciE'
