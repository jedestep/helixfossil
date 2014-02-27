import client
import win32api
import win32con
import time

class HelixClientW32(client.HelixClient):
    def keypress(self, key):
        win32api.keybd_event(self.ctrl[key],0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(self.ctrl[key],0,win32con.KEYEVENTF_KEYUP,0)

if __name__ == "__main__":
    client = HelixClientW32(
        dict(a=0x5a,
             b=0x58,
             left=0x46,
             right=0x48,
             down=0x47,
             up=0x54,
             l=0x41,
             r=0x53,
             select=0x4A,
             start=0x4B),
        4242)  # TODO find next available port from server
    client.listen_forever()
