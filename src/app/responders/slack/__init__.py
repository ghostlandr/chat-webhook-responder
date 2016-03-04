""" __init__.py.py """
import json

from webapp2 import RequestHandler

from app.responders import BaseResponder


class SlackResponderMixin(RequestHandler, BaseResponder):
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

    @staticmethod
    def prepare_string(args):
        return args['text'].split(':')[1]
