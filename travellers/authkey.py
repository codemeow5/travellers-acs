#!/usr/bin/python

import sys, os, threading
import tornado.web
import tornado.gen
import logging

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('..')
import common
import config

logger = logging.getLogger('web')

class AuthKeyHandler(common.RequestHandler):

	@tornado.gen.coroutine
	def post(self):
		pass

