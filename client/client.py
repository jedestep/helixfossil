import socket

class HelixClient(object):
    def __init__(self, ctrl, port):
        self.ctrl = ctrl
        self.port = port

    # Overwrite per implementation
    def keypress(self, key):
        pass

    def listen_forever(self):
        s = socket.socket()
        s.connect(('www.helixfossil.tv', self.port))
        try:
            while True:
                content = s.recv(1024)
                if len(content) > 0 and content in self.ctrl.keys():
                    self.keypress(content)
        except KeyboardInterrupt:
            pass
        s.close()
