#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append('../')

from game.Db import db
from bson.objectid import ObjectId

class Scene(object):
    """
    游戏场景类
    初始化scene时必须指定 sid
    若要新建场景,则可以调用 Scene 的静态类 Scene.create() 来实现
    """
    db = db
    def __init__(self, sid):
        self.sid = ObjectId(sid) # 转换str 为 objectid
        self.scene = self.db.scene.find_one({'_id':self.sid})

    def __get(self, attr, default=''):
        """
        根据 attribute 的值返回场景指定的属性
        default 为默认值,即当数据不存在时返回的值
        """
        result = self.db.scene.find_one({'_id':self.sid}, projection={attr:True})
        return result.get(attr, default) if result else None

    def __set(self, attr, value):
        """
        根据 attribute 的值设置
        """
        from pymongo import ReturnDocument
        result = self.db.scene.find_one_and_update({'_id': self.sid},
                                                    {'$set':{attr:value}},
                                                    return_document=ReturnDocument.AFTER)

        return result.get(attr) if result else False

    def ops(self):
        """
        场景所包含的操作
        返回值为列表
        """
        result = self.db.scene.find_one({'_id':self.sid}, projection={'ops':True})

        return result.get('ops', [])

    @property
    def events(self):
        """
        场景所有的事件
        创建,查看,进入, 离开 , 分钟定时
        """
        result = self.db.scene.find_one({'_id': self.sid}, projection={'events':True})
        return result.get('events', [])

    @property
    def npc(self):
        """
        场景所包含的npc
        返回值为列表
        """
        result = self.db.scene.find_one({'_id':self.sid}, projection={'npc':True})
        return result.get('npc', [])

    @property
    def items(self):
        """
        场景中的物品
        """
        result = self.db.scene.find_one({'_id':self.sid}, projection={'items': True})
        return result.get('items', [])


    @classmethod
    def create(cls, data=dict()):
        """
        创建场景,直接 insert
        """
        return True
        # pass

    def update(cls, data=dict()):
        """
        批量更新场景数据
        """
        pass

    @property
    def pic(self):
        '''图片'''
        return self.__get('pic')

    @pic.setter
    def pic(self, value):
        return self.__set('pic', value)

    @property
    def name(self):
        '''名称'''
        return self.__get('name')

    @name.setter
    def name(self, value):
        return self.__set('name', value)

    @property
    def desc(self):
        '''描述'''
        return self.__get('desc')

    @desc.setter
    def desc(self, value):
        return self.__set('desc', value)

    @property
    def refresh(self):
        '''刷新间隔'''
        return self.__get('refresh', default=3)

    @refresh.setter
    def refresh(self, value):
        return self.__set('refresh', value=3)

    @property
    def is_safety(self):
        '''是否是安全区'''
        return self.__get('is_safety', default=True)

    @is_safety.setter
    def is_safety(self, value=True):
        return self.__set('is_safety', value)


if __name__ == '__main__':
    a1 = Scene('58d0b8a4b4851837d6c1f2c1')
    # a1.name = '长南村广场'
    # a1.is_safety = False
    print(a1.items)
