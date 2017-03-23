#!/usr/bin/env python
# coding=utf-8
#  游戏场景测试文件

import sys
sys.path.append('../')

from game import Scene
import unittest

class Scene_test(unittest.TestCase):

    def setUp(self):
        '''初始化'''
        self.scene = Scene('58d0b8a4b4851837d6c1f2c1')

    def test_name(self):
        '''场景名称'''
        self.assertIsInstance(self.scene.name, str)

    def test_refresh(self):
        '''刷新时间'''
        self.assertTrue(self.scene.refresh)
        self.assertIsInstance(self.scene.refresh, int)

    def test_desc(self):
        '''场景简介'''
        self.assertIsInstance(self.scene.desc, str)

    def test_pic(self):
        '''场景图片'''
        self.assertIsInstance(self.scene.pic, str)

    def test_is_safety(self):
        '''是否是安全区'''
        self.assertIsInstance(self.scene.is_safety, bool)

    def test_ops(self):
        '''场景所含操作'''
        self.assertIsInstance(self.scene.ops(), list)

    def test_events(self):
        '''场景事件'''
        self.assertIsInstance(self.scene.events, dict)

    def test_npc(self):
        '''场景npc'''
        self.assertIsNotNone(self.scene.npc)
        self.assertIsInstance(self.scene.npc, list)

    # def

if __name__ == '__main__':
    unittest.main()
