""" __init__.py.py """
import json
import logging

from webapp2 import RequestHandler

from app.responders import BaseResponder


class HipChatResponderMixin(RequestHandler, BaseResponder):
    """
    Base responder that knows the formats HipChat sends/expects.
    """
    def post(self):
        """
        Receive the post! HipChat requests come in as a JSON-encoded post body.
        """
        post_body = json.loads(self.request.body)
        logging.info(self.request.body)
        if self.check_credentials(post_body['webhook_id']):
            self.render_response({'message': self.process(post_body)})
        else:
            self.abort(401)

    def render_response(self, args):
        return self.response.write(json.dumps({
            'color': args.get('color', 'green'),
            'message': args['message'],
            'notify': args.get('notify', False),
            'message_format': args.get('message_format', 'text')
        }))

    @staticmethod
    def prepare_string(args):
        return args['text'].split(':')[1]
