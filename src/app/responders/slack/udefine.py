""" udefine.py """
from app.responders.common.udefine import UDefineResponder
from app.responders.slack import SlackResponderMixin

from settings import UDEFINE_TOKENS


class UDefineSlackResponder(UDefineResponder, SlackResponderMixin):
    """
    Responds to /udefine/slack/ requests
    """
    @classmethod
    def check_credentials(cls, token):
        return token in UDEFINE_TOKENS[cls.PLATFORM]
