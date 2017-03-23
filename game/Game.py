#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append('../')

from game.Db import db
from bson.objectid import ObjectId

class Game(object):
    """
    游戏基本信息类
    """
    def __init__(self, gid):
        self.gid = ObjectId(gid) # 游戏id
        self.game = db.game

    def __get(self, attr, default=''):
        """
        根据 attribute 的值返回场景指定的属性
        default 为默认值,即当数据不存在时返回的值
        """
        result = self.game.find_one({'_id':self.gid}, projection={attr:True})
        return result.get(attr, default)

    def __set(self, attr, value):
        """
        根据 attribute 的值设置
        """
        from pymongo import ReturnDocument
        result = self.game.find_one_and_update({'_id': self.gid},
                                                    {'$set':{attr:value}},
                                                    return_document=ReturnDocument.AFTER)
        return result.get(attr) if result else False

    @property
    def name(self):
        '''游戏名称'''
        return self.__get('name')

    @name.setter
    def name(self, value):
        return self.__set('name', value)

    @property
    def desc(self):
        '''游戏介绍'''
        return self.__get('desc')

    @desc.setter
    def desc(self, value):
        return self.__set('desc', value)

    @property
    def money(self):
        '''货币信息'''
        return self.__get('money', {})

    @money.setter
    def money(self, values):
        # print(isinstance(value, dict))
        if isinstance(values, dict) is not True:
            print("类型错误,参数必须为字典")

        try:
            if 'name' in values:
                name = self.__set('money.name', values.get('name'))
            if 'unit' in values:
                unit = self.__set('money.unit', values.get('unit'))
            return True
        except:
            return False



if __name__ == '__main__':
    g1 = Game('58d364e9b4851837d6c239ae')
    g1.money = {'name':'银子'}
