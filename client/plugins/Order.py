# -*- coding: utf-8-*-
import datetime
from client.app_utils import getTimezone
from semantic.dates import DateService

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

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    service = DateService()
    response = service.convertTime(now)
    mic.say(u"尊敬的客户，您当前有处理中的订单數100张， %s " % response)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in ["订单"])
