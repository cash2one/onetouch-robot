# -*- coding: utf-8-*-
import urllib2
import json

WORDS = [u"BUSINESSNEWS", u"WAIMAO", u"XINWEN"]
SLUG = "businessnews"


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

    # 'https://widget.1688.com/front/getJsonComponent.json?page=1&length=10&key=osap_wmq_query_hot_content&querymap=%7B%22childCid%22%3A999%7D&namespace=GetContentList&widgetId=GetContentList&methodName=execute'
    # 'referer: https://waimaoquan.alibaba.com/' - -compressed

    mic.say(u"正在为您查找您感兴趣的新闻。")

    mic.say(u"为您找到十条最新新闻，第一条内容为，B2B内参消息 2017年12月25日，工程机械互联网综合服务平台铁甲对外宣布，已完成逾5000万美元的C+轮融资")

    url = 'https://widget.1688.com/front/getJsonComponent.json?page=1&length=10&key=osap_wmq_query_hot_content&querymap=%7B%22key%22%3A%22%E6%9C%BA%E6%A2%B0%22%7D&namespace=GetContentList&widgetId=GetContentList&methodName=execute'

    headers = {
        'referer': 'https://waimaoquan.alibaba.com/'
    }

    req = urllib2.Request(url, headers=headers)
    req.get_method = lambda: 'HEAD'
    res = urllib2.urlopen(req)

    data=res.read()

    print data

    # json_data = json.dumps(data)
    # print json_data

    # print json.loads(json_data)["content"]

    # mic.say(u"是否需要订阅？")/


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in ["新闻","外贸新闻","外贸信息","外贸咨询"])
