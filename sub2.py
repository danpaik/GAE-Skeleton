import cgi
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import logging
import datetime
import hashlib

from google.appengine.ext.webapp import template
from gaesessions import get_current_session
from gaesessions import delete_expired_sessions

import settings
from models import *

class Sub2Index(webapp.RequestHandler):
	def get(self):
		template_values = {}
		template_values['CDN_HOST'] = settings.CDN_HOST
		path = os.path.join(os.path.dirname(__file__), 'templates/sub2/index.html')
		logging.info("path %s" % (path))
		self.response.out.write(template.render(path, template_values))

class Sub2About(webapp.RequestHandler):
	def get(self):
		template_values = {}
		template_values['CDN_HOST'] = settings.CDN_HOST
		path = os.path.join(os.path.dirname(__file__), 'templates/sub2/about.html')
		logging.info("path %s" % (path))
		self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
									[
									('/sub2/index', Sub2Index),
									('/sub2/about', Sub2About),
									],
									debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()