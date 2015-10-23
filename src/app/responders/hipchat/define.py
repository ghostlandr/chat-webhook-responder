""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.hipchat import HipChatResponderMixin

from settings import DEFINE_TOKENS


class DefineHipChatResponder(DefineResponder, HipChatResponderMixin):
    @staticmethod
    def check_credentials(token):
        return token in DEFINE_TOKENS['hipchat']

    def process(self, args):
        term = args['item']['message']['message'].split('/')[1][len(self.KEY_WORD):].strip()

        return self.get_definitions(term)
