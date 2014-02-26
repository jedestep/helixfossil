#!/usr/bin/python
import thread
import BaseHTTPServer
import SimpleHTTPServer
import time
import socket

HOSTNAME = socket.gethostname()
PORT_NUMBER = 80

class CommandConnectionException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CommandConnection(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((socket.gethostname(), 4242))
        self.sock.listen(5)
        self.clientsock = None
        self.dead = False

    def connect(self):
        if self.dead:
            raise CommandConnectionException("cannot open connection on dead socket")
        clientsocket, addr = self.sock.accept()
        print "Connected to", addr
        self.clientsock = clientsocket

    def send(self,msg):
        try:
            if self.clientsock is not None:
                self.clientsock.send(msg)
        except IOError:
            self.clientsock = None  # toss the old socket
            for i in xrange(0,5):
                if self.clientsock is not None:
                    break
                thread.start_new_thread(self.connect, ())
            
            
class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    csock = None
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
    print "sending", content
    if self.csock is not None:
        if not self.csock.dead:
            self.csock.send(content)
        self.send_response(200)

if __name__ == '__main__':
    c = CommandConnection()
    thread.start_new_thread(c.connect, ())
    RequestHandler.csock = c
    httpd = BaseHTTPServer.HTTPServer((HOSTNAME, PORT_NUMBER), RequestHandler)
    print "Server start :: " + time.asctime()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "\nServer stop :: " + time.asctime()
