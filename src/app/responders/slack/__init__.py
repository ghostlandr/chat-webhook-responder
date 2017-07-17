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
        token = self.request.POST.get('token')
        if not token:
            self.abort(401)

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


class SlackCommandResponder(RequestHandler, BaseResponder):
    """
    Base responder for Slacks' custom integration slash commands
    """
    RESPONSE_TYPE = None # Set to "in_channel" for response & message to be shared in channel

    def post(self):
        """ POST """
        token = self.request.POST.get('token')
        if not token:
            self.abort(401)

        if self.check_credentials(token):
            response = {
                "text": self.process(self.request.POST)
            }
            attachment = self.build_attachment()
            if self.RESPONSE_TYPE:
                response["response_type"] = self.RESPONSE_TYPE
            if attachment:
                response["attachment"] = attachment
            self.render_response(response)
        else:
            self.abort(401)

    def process(self, args):
        """ process """
        raise NotImplementedError()

    @classmethod
    def check_credentials(cls, token):
        return token in cls.TOKENS['slack']

    def render_response(self, args):
        return self.response.write(json.dumps(args))

    def build_attachment(self):
        """
        Build list of attachments as follows:
        [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                "pretext": "Optional text that appears above the attachment block",
                "author_name": "Bobby Tables",
                "author_link": "http://flickr.com/bobby/",
                "author_icon": "http://flickr.com/icons/bobby.jpg",
                "title": "Slack API Documentation",
                "title_link": "https://api.slack.com/",
                "text": "Optional text that appears within the attachment",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": false
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Slack API",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": 123456789
            }
        ]
        """
        return []

    def prepare_string(args):
        pass

