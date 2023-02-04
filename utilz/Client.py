import socket
from utilz.method import *
from utilz.constant import *
from utilz.RC4 import *

class Client:
    def __init__(self, host, port, key):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOURCE_PORT = 51055
        while True:
            try:
                self.s.bind(('0.0.0.0', self.SOURCE_PORT))
                break
            except:
                print(f"PORT {self.SOURCE_PORT} is used, try to another PORT...")
                self.SOURCE_PORT+=1
        self.server_address = (host, port)
        self.key = key
        # self.connect()
    
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
        dataEnc = enc(self.key, data)
        msg = msgWithHeader(dataEnc, HEADER)
        self.s.sendall(msg)

    def sendFileName(self, name):
        msg = name.encode("utf8")
        msgEnc = enc(self.key, msg)
        msg = msgWithHeader(msgEnc, HEADER)
        self.s.sendall(msg)
    
    def sendInt(self, num):
        data = num.to_bytes(4, 'big')
        dataEnc = enc(self.key, data)
        self.s.sendall(dataEnc)

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
        return dec(self.key, self.recv_all(length))

    def recvInt(self):
        data = dec(self.key, self.recv_all(4))
        return int.from_bytes(data, 'big')


