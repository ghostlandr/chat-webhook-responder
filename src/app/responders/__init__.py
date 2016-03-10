"""
__init__.py
"""


class BaseResponder(object):
    @classmethod
    def check_credentials(cls, token):
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
        raise NotImplementedError()

    @staticmethod
    def prepare_string(args):
        """
        Defined in child class to be either a HipChat or Slack specific string preparation function.

        :param args: json.loads'd args provided by either Slack or HipChat
        :return: Cleaned text string that can be operated on by the responder, agnostic of chat client.
        """
        raise NotImplementedError()
