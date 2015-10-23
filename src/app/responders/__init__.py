"""
__init__.py
"""


class BaseResponder(object):
    @staticmethod
    def check_credentials(token):
        """
        Defined in child class.
        """
        raise NotImplementedError()

    def process(self, args):
        """
        Defined in child class.
        """
        raise NotImplementedError()

    def render_response(self, args):
        """
        Defined in child class.
        """
        raise NotImplementedError
