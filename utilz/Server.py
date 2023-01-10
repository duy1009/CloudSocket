
import socket
import glob
from utilz.method import *
from utilz.constant import *

class Server:
    def __init__(self, host, port, num = 5):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(num)
        self.connect()

    def connect(self):
        print("Connecting...")
        while True:
            try: 
                self.client, self.addr = self.s.accept()
                print('Connected by', self.addr)
                break
            except:
                print("Listen to client...")
    
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