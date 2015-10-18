""" Entry point for the app """
from webapp2 import Route, WSGIApplication


ROUTES = [
    Route('/define', handler='app.views.define.DefineView'),
]


APP = WSGIApplication(routes=ROUTES)
