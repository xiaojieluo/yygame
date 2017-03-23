#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options

from app import route
from app.setting import config
define("port", default=8888, help="run on the given port", type=int)

def make_app():
    return tornado.web.Application(
        handlers=route,
        **config
    )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    apps = make_app()
    http_server = tornado.httpserver.HTTPServer(apps)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
