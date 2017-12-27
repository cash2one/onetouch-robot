# -*- coding: utf-8-*-
WORDS = [u"PARTNER", u"PAIDANG"]
SLUG = "partner"


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
    mic.say(u"正在为您拨打拍档电话 ")



def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in ["联系拍档","连续拍照"])
