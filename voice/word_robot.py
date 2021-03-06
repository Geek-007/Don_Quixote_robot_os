#!/usr/bin/python
# -*- coding: utf8 -*-
"""
使用百度对图灵机器人作为基础语言聊天机器人
"""
import json
import urllib2
import sys
from control.settings import ChatFather
reload(sys)
sys.setdefaultencoding('utf-8')

class Chat(ChatFather):
    def send(self,info):
        url = self.apiurl + 'key=' + self.key + '&' + 'info=' + info
        url = url.decode('utf-8')
        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        text = re_dict['text']
        return text.decode('utf-8')

chat = Chat()
def robot(words):
    return chat.send(words)
