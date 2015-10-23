""" Entry point for the app """
from webapp2 import WSGIApplication

from urls import ROUTES


APP = WSGIApplication(routes=ROUTES)
