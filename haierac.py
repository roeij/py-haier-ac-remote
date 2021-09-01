from haierlib.types import *
from haierlib.parsers import *
import socket

class HaierAC:
    def __init__(self, ip, mac, port = 56800, timeout = 500) -> None:
        self._ip = ip
        self._port = port
        self._mac = mac
        self._timeout = timeout
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._seq = 0

    def test_recv_loop(self):
        self._sock.connect((self._ip, self._port))
        while True:
            recv_data = self._sock.recv(1000)
            if recv_data:
                print("-- Has Data --")
                print(parse_resp(recv_data))

    # TODO complete socket functions

    # TODO complete send behavior functions
    def send_hello(self):
        pass

    def send_init(self):
        pass

    def send_on(self):
        pass

    def send_off(self):
        pass

    def change_State(self):
        pass
