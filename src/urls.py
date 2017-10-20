""" urls.py """
from webapp2 import Route


ROUTES = [
    Route('/define/slack', handler='app.responders.common.define.DefineSlackResponder'),
    Route('/define/hipchat', handler='app.responders.hipchat.define.DefineHipChatResponder'),
    Route('/udefine/slack', handler='app.responders.common.udefine.UDefineSlackResponder'),
    Route('/udefine/hipchat', handler='app.responders.hipchat.udefine.UDefineHipChatResponder'),
    Route('/dndefine/slack', handler='app.responders.common.dndefine.DndefineSlackResponder'),
    Route('/cal/slack', handler='app.responders.common.cal.CalSlackResponder'),
    Route('/cal/random', handler='app.responders.common.random_selector.RandomSelectorResponder'),

]
