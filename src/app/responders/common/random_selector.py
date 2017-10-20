""" random_selector.py """
import random

from app.responders.slack import SlackCommandResponder

from settings import RANDOM_SELECTION_TOKENS


class RandomSelectorResponder(SlackCommandResponder):
    """ Respond to requests for /random commands """

    TOKENS = RANDOM_SELECTION_TOKENS
    RESPONSE_TYPE = "in_channel"

    def process(self, args):
        """
        """
        return random.choice(args["text"].replace(" ", "").split(','))




