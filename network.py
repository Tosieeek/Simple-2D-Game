import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.56"
        self.port = 5555
        self.addr = (self.server, self.port)

        try:
            self.client.connect(self.addr)
        except:
            pass


    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))

            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

