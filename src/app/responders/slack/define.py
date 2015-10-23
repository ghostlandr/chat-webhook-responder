""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.slack import SlackResponderMixin
from settings import DEFINE_TOKENS


class DefineSlackResponder(DefineResponder, SlackResponderMixin):
    @staticmethod
    def check_credentials(token):
        return token in DEFINE_TOKENS['slack']

    def process(self, args):
        text = args['text']
        term = text.split(':')[1].strip()

        return self.get_definitions(term)
