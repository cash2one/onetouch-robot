# -*- coding: utf-8-*-
import os

import time

from subprocess import check_output

import re

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

    os.system("/usr/bin/linphonecsh generic 'call 8000 --audio-only'")

    call_ended = False

    while not call_ended:
        time.sleep(2)
        output = check_output(['/usr/bin/linphonecsh', 'generic', 'calls'])
        if re.compile("No active call").match(output):
            call_ended = True
        else:
            print 'still calling'


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    print "====================="
    print(text)
    print(re.compile("(联系|连线|连续|电话).*(拍档|拍照|拍大)").match(text));
    print("=====================")
    return re.compile("(联系|连线|连续|电话).*(拍档|拍照|拍大)").match(text)
    # return any(word in text for word in ["联系拍档","连续拍照","联系拍照"])
