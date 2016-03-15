""" greeter.py """
from app.responders.slack import SlackResponder
from settings import GREETER_TOKENS


class GreeterResponder(object):
    TOKENS = GREETER_TOKENS

    def process(self, args):
        user = args['user_name']
        return u'Hello {}'.format(user)


class GreeterSlackResponder(GreeterResponder, SlackResponder):
    """
    Greets people in Slack.
    """
