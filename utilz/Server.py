
import socket
import glob
from utilz.method import *
from utilz.constant import *
from utilz.RC4 import *

class Server:
    def __init__(self, client, addr, key):
        self.client, self.addr = client, addr
        self.key = key
    
    def sendListOfData(self, folder):
        folData = glob.glob(folder+"\\*")
        msg = convList1DToByte(folData,"|")
        # list = convByteToList1D(msg, "|")
        msgEnc = enc(self.key, msg)
        msg = msgWithHeader(msgEnc, HEADER)
        self.client.sendall(msg)

    def sendFile(self, path):
        f = open(path, 'rb')
        data = f.read()
        f.close()
        dataEnc = enc(self.key, data)
        msg = msgWithHeader(dataEnc, HEADER)
        self.client.sendall(msg)
    
    def sendFileName(self, name):
        msg = name.encode("utf8")
        msgEnc = enc(self.key, msg)
        msg = msgWithHeader(msgEnc, HEADER)
        self.client.sendall(msg)

    def sendInt(self, num):
        data = num.to_bytes(4, 'big')
        dataEnc = enc(self.key, data)
        self.client.sendall(dataEnc)

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
        return dec(self.key, self.recv_all(length))
    def recv_raw_data(self, header):
        length_byte = self.recv_all(header)
        length = int.from_bytes(length_byte, 'big')
        return self.recv_all(length)
    def recvInt(self):
        data = dec(self.key, self.recv_all(4))
        return int.from_bytes(data, 'big')
    def close(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
    # print(list)