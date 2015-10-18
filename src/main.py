""" Entry point for the app """
from webapp2 import Route, WSGIApplication


ROUTES = [
    Route('/define', handler='app.responders.define.DefineResponder'),
]


APP = WSGIApplication(routes=ROUTES)
