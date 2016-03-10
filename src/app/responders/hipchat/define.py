""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.hipchat import HipChatResponderMixin

from settings import DEFINE_TOKENS


class DefineHipChatResponder(DefineResponder, HipChatResponderMixin):
    PLATFORM = 'hipchat'

    def process(self, args):
        term = self.prepare_string(args)[len(self.KEY_WORD):].strip()

        return self.get_definitions(term)
