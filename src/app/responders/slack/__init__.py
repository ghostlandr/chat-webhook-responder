""" __init__.py.py """
import json

from webapp2 import RequestHandler

from app.responders import BaseResponder


class SlackResponder(RequestHandler, BaseResponder):
    """
    Base responder that knows the formats Slack sends/expects.
    """
    def post(self):
        """
        Receive the post!
        """
        token = self.request.POST['token']

        if self.check_credentials(token):
            self.render_response({'text': self.process(self.request.POST)})
        else:
            self.abort(401)

    def render_response(self, args):
        return self.response.write(json.dumps({
            'text': args['text']
        }))

    def process(self, args):
        raise NotImplementedError()

    @classmethod
    def check_credentials(cls, token):
        return token in cls.TOKENS['slack']

    @staticmethod
    def prepare_string(args):
        trigger_word = args['trigger_word']
        if trigger_word.rfind(':') == -1:
            trigger_word += ':'
        return args['text'].split(trigger_word)[1].strip()
