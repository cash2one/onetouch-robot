# -*- coding: utf-8-*-
import datetime
from client.app_utils import getTimezone
from semantic.dates import DateService
import urllib2

WORDS = [u"MESSAGE", u"XIAOXI"]
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

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    service = DateService()
    response = urllib2.urlopen('http://30.135.15.126:8080/api/message')
    mic.say(u"尊敬的客户，收到一条消息，消息内容为：， %s " % response.read())


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in ["消息"])
