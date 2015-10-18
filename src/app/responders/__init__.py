"""
__init__.py
"""
import json
from webapp2 import RequestHandler


class BaseResponder(RequestHandler):

    @staticmethod
    def check_credentials(token):
        """
        Defined in child class.

        :param token: str An authentication token for a Slack integration.
        """
        raise NotImplementedError()

    def process(self, text, trigger_word):
        """
        Defined in child class. Should return a string of text to send back to Slack.

        :param text: str The full text of what the user passed in.
        :param trigger_word: str The word that triggered this call.
        """
        raise NotImplementedError()

    def post(self):
        """
        Slack will post to a URL. Receive the post!
        """
        token = self.request.POST['token']
        text = self.request.POST['text']
        trigger_word = self.request.POST['trigger_word']

        if self.check_credentials(token):
            self.render_slack_reponse(self.process(text, trigger_word))
        else:
            self.abort(401)

    def render_slack_reponse(self, text, attachments=None):
        """
        Write out in a format Slack expects. Attachments are not supported at this time.
        """
        return self.response.write(json.dumps({
            'text': text
        }))
