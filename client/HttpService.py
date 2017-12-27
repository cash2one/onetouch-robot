#!/usr/bin/env python
# coding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from pygame import mixer
from threading import Thread
from urlparse import urlparse, parse_qs

instance = None


def play_audio(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()


class HttpServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self.address_string())
        params = parse_qs(urlparse(self.path).query)
        if params.has_key('text'):
            instance.mic.say(params['text'][0])
        elif params.has_key('file'):
            play_audio("/home/pi/dingdang/static/audio/" + params['file'][0])

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


class HttpService:
    def __init__(self, bot):
        global instance
        instance = bot
        httpd = HTTPServer(('', 8888), HttpServiceHandler)
        print 'Starting http services...'
        thread = Thread(target=httpd.serve_forever, args=())
        thread.setDaemon(True)
        thread.start()
