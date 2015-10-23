""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.hipchat import HipChatResponderMixin


class DefineHipChatResponder(DefineResponder, HipChatResponderMixin):

    def process(self, args):
        term = args['item']['message']['message'].split('/')[1][len(self.KEY_WORD):].strip()

        return self.get_definitions(term)
