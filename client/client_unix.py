import client
import uinput

class HelixClientUNIX(client.HelixClient):
    def __init__(self, ctrl, port):
        client.HelixClient.__init__(self, ctrl, port)
        self.device = uinput.Device([
            uinput.KEY_Z,
            uinput.KEY_X,
            uinput.KEY_T,
            uinput.KEY_F,
            uinput.KEY_G,
            uinput.KEY_H,
            uinput.KEY_K,
            uinput.KEY_J,
            uinput.KEY_A,
            uinput.KEY_S
            ])

    def keypress(self, key):
        self.device.emit_click(self.ctrl[key])

if __name__ == "__main__":
    client = HelixClientUNIX(
        dict(a=uinput.KEY_Z,
             b=uinput.KEY_X,
             up=uinput.KEY_T,
             left=uinput.KEY_F,
             down=uinput.KEY_G,
             right=uinput.KEY_H,
             start=uinput.KEY_K,
             select=uinput.KEY_J,
             l=uinput.KEY_A,
             r=uinput.KEY_S)
        4242)  # TODO find next available port from server
    client.listen_forever
