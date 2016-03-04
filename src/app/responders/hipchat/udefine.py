""" udefine.py """
from app.responders.common.udefine import UDefineResponder
from app.responders.hipchat import HipChatResponderMixin

from settings import UDEFINE_TOKENS


class UDefineHipChatResponder(UDefineResponder, HipChatResponderMixin):
    @staticmethod
    def check_credentials(token):
        return token in UDEFINE_TOKENS['hipchat']

    def process(self, args):
        term = ' '.join(args['item']['message']['message'].split('/')[1].split(' ')[1:]).strip()

        return self.get_definitions(term)
