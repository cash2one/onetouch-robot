# -*- coding: utf-8-*-
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
    mic.say(u"尊敬的客户，您的订单 东疆港区到澳大利亚的订单119186-26208状态在今天下午3:55分由办理中变为已完成 ")


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in ["订单"])
