# -*- coding: utf-8-*-
import datetime
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = [u"NOTES", u"ZHUYI", u"SHIXIANG"]
SLUG = "message"


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
    service = DateService()
    mic.say(u"尊敬的客户，注意事项如下：公告自2017年11月1日起施行。具体时间以出口货物报关单上注明的出口日期为准。《国家税务总局关于外贸综合服务企业出口货物退(免)税有关问题的公告》（国家税务总局公告2014年第13号）同时废止。 ")


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return all(word in text for word in ["注意","事项"])
