""" urls.py """
from webapp2 import Route


ROUTES = [
    Route('/define/slack', handler='app.responders.slack.define.DefineSlackResponder'),
    Route('/define/hipchat', handler='app.responders.hipchat.define.DefineHipChatResponder'),
    Route('/udefine/slack', handler='app.responders.slack.udefine.UDefineSlackResponder'),
    Route('/udefine/hipchat', handler='app.responders.hipchat.udefine.UDefineHipChatResponder'),
]
