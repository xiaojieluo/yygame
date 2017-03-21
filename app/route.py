#!/usr/bin/env python
# coding=utf-8

import tornado.web
from .handler import IndexHandler as Index

route = [
    (r'/', Index.index),
]
