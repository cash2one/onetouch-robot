# -*- coding: utf-8-*-
import re
import random

WORDS = [u"ORDER", u"DINGDAN"]
SLUG = "order"


def handle(text, mic, profile, wxbot=None):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
        wxBot -- wechat robot
    """
    messages = [u"为您找到一条最新订单动态，订单号为一一九一八六-二六二零八从深圳大鹏海关到澳大利亚的订单状态已由待受理变为待上传通关单",
                u"抱歉，没有查到最新订单动态，请登录一达通MO客户操作平台进行下单",
                u"为您找到一条最新订单动态，订单号为一一九一八六-二六二四零从外高桥关到亚美尼亚的订单状态已由受理中变为待报关",
                u"为您找到一条最新订单动态，订单号为一一九一八六-二六二四零保税物流到安道尔的订单状态已由受理中变为待签函"]
    message = random.choice(messages)
    mic.say(message)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return re.compile("(查询|最新|我的).*订单(状态)?").match(text)
