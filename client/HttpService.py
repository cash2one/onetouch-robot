#!/usr/bin/env python
# coding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import call
from threading import Thread
from urlparse import urlparse, parse_qs

instance = None


def play_audio(path):
    call("mpv " + path + " --no-video --no-config --force-window=no &", shell=True)
    # mixer.init()
    # mixer.music.load(path)
    # mixer.music.play()


class HttpServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self.address_string())
        params = parse_qs(urlparse(self.path).query)
        if 'text' in params:
            instance.mic.say(params['text'][0])
        elif 'enable' in params:
            instance.mic.stop_listening = False
        elif 'disable' in params:
            instance.mic.stop_listening = True
        elif 'dial' in params:
            call(["/usr/bin/linphonecsh", "dial", "8000"])
        elif 'terminate' in params:
            call(["/usr/bin/linphonecsh", "generic", "terminate"])
        elif 'file' in params:
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
