
import socket
import glob
from utilz.method import *
from utilz.constant import *

class Server:
    def __init__(self, client, addr):
        self.client, self.addr = client, addr
    
    def sendListOfData(self, folder):
        folData = glob.glob(folder+"\\*")
        msg = convList1DToByte(folData,"|")
        # list = convByteToList1D(msg, "|")
        msg = msgWithHeader(msg, HEADER)
        self.client.sendall(msg)

    def sendFile(self, path):
        f = open(path, 'rb')
        data = f.read()
        f.close()
        msg = msgWithHeader(data, HEADER)
        self.client.sendall(msg)
    
    def sendFileName(self, name):
        msg = name.encode("utf8")
        msg = msgWithHeader(msg, HEADER)
        self.client.sendall(msg)

    def sendInt(self, num):
        data = num.to_bytes(4, 'big')
        self.client.sendall(data)

    def recv_all(self, length):
        data = self.client.recv(length)
        while True:
            miss_len_data = length - len(data)
            if miss_len_data==0:
                break
            data += self.client.recv(miss_len_data)
        return data

    def recv_data(self, header): 
        length_byte = self.recv_all(header)
        length = int.from_bytes(length_byte, 'big')
        return self.recv_all(length)

    def recvInt(self):
        data = self.recv_all(4)
        return int.from_bytes(data, 'big')

    # print(list)