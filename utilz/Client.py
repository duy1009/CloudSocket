import socket
from utilz.method import *
from utilz.constant import *

class Client:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.connect()
    
    def connect(self):
        print("Connecting...")
        print("Waiting server...")
        while True:
            try:
                self.s.connect(self.server_address)
                break
            except:
                ()

    def sendFile(self, path):
        f = open(path, 'rb')
        data = f.read()
        print(f"Size of file: {len(data)} bytes")
        f.close()
        msg = msgWithHeader(data, HEADER)
        self.s.sendall(msg)

    def sendFileName(self, name):
        msg = name.encode("utf8")
        msg = msgWithHeader(msg, HEADER)
        self.s.sendall(msg)
    
    def sendInt(self, num):
        data = num.to_bytes(4, 'big')
        self.s.sendall(data)

    def recv_all(self, length):
        data = self.s.recv(length)
        while True:
            miss_len_data = length - len(data)
            if miss_len_data==0:
                break
            data += self.s.recv(miss_len_data)
        return data

    def recv_data(self, header): 
        length_byte = self.recv_all(header)
        length = int.from_bytes(length_byte, 'big')
        return self.recv_all(length)

    def recvInt(self):
        data = self.recv_all(4)
        return int.from_bytes(data, 'big')


