""" udefine.py """
from app.responders.common.udefine import UDefineResponder
from app.responders.slack import SlackResponderMixin

from settings import UDEFINE_TOKENS


class UDefineSlackResponder(UDefineResponder, SlackResponderMixin):
    @staticmethod
    def check_credentials(token):
        return token in UDEFINE_TOKENS['slack']

    def process(self, args):
        term = ' '.join(self.prepare_string(args).split(' ')[1:]).strip()

        return self.get_definitions(term)
