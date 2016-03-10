""" udefine.py """
from app.responders.common.udefine import UDefineResponder
from app.responders.hipchat import HipChatResponderMixin

from settings import UDEFINE_TOKENS


class UDefineHipChatResponder(UDefineResponder, HipChatResponderMixin):
    @staticmethod
    def check_credentials(token):
        return token in UDEFINE_TOKENS['hipchat']

    def process(self, args):
        term = ' '.join(self.prepare_string(args).split(' ')[1:]).strip()

        return self.get_definitions(term)
