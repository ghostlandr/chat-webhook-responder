""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.slack import SlackResponderMixin
from settings import DEFINE_TOKENS


class DefineSlackResponder(DefineResponder, SlackResponderMixin):
    PLATFORM = 'slack'

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))
