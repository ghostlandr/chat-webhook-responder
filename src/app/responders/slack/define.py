""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.slack import SlackResponder


class DefineSlackResponder(DefineResponder, SlackResponder):

    def process(self, args):
        return self.get_definitions(self.prepare_string(args))
