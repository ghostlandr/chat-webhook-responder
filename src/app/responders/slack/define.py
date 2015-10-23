""" define.py """
from app.responders.common.define import DefineResponder
from app.responders.slack import SlackResponderMixin


class DefineSlackResponder(DefineResponder, SlackResponderMixin):

    def process(self, args):
        text = args['text']
        term = text.split(':')[1].strip()

        return self.get_definitions(term)
