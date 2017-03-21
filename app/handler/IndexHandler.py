#!/usr/bin/env python
# coding=utf-8

import tornado.web
from .BaseHandler import BaseHandler

class index(BaseHandler):
    def get(self):
        self.write("Hello yygame!")
