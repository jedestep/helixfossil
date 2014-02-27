#!/usr/bin/python
import thread
import CGIHTTPServer
import time
import socket

HOSTNAME = socket.gethostname()
PORT_NUMBER = 80

next_port = 4242
glines = open(".games", "r").readlines()

class CommandConnectionException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CommandConnection(object):
    def __init__(self):
        global next_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((socket.gethostname(), next_port))
        next_port += 1
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
            
            
class RequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
    csocks = None
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length).split("|")
        streamname = content[0].strip()
        msg = content[1].strip()
        if self.csocks is not None:
            csock = self.csocks[streamname]
            if csock is not None and not csock.dead:
                print "sending", msg, "to", csock.sock.getsockname()
                csock.send(msg)
            self.send_response(200)

if __name__ == '__main__':
    csocks = {}
    for line in glines:
        streamname = line.split("|")[0].strip()
        c = CommandConnection()
        thread.start_new_thread(c.connect, ())
        csocks.update({streamname: c})
    RequestHandler.csocks = csocks
    RequestHandler.cgi_directories = ['/cgi']
    httpd = CGIHTTPServer.BaseHTTPServer.HTTPServer((HOSTNAME, PORT_NUMBER), RequestHandler)
    print "Server start :: " + time.asctime()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "\nServer stop :: " + time.asctime()
