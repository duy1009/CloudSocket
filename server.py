import os
from utilz.method import *
from utilz.constant import *
from utilz.Server import Server

dataPath = "./Data"
HOST='localhost'
PORT=8000

server = Server(HOST, PORT, 5)

while True:
    server.sendListOfData(dataPath)
    option = server.recvInt()

    if (option == 2):
        file_name = server.recv_data(HEADER).decode("utf8")
        data = server.recv_data(HEADER)

        file_path = dataPath+"/"+file_name
        status = saveData(file_path, data)
        server.sendInt( status) # status feedback
    elif (option == 3):
        file_name = server.recv_data(HEADER).decode("utf8")
        full_path = dataPath + "/" + file_name
        
        if os.path.isfile(full_path): # check file
            status = 2
        else: status = 3
        server.sendInt(status) # send status
        
        if status == 2: # send file
            server.sendFile(full_path)
    elif option == 4:
        file_name = server.recv_data(HEADER).decode("utf8")
        full_path = dataPath + "/" + file_name
        
        if os.path.isfile(full_path): # check file
            os.remove(full_path)
            print("Deleted")
            status = 0
        else: status = 3
        server.sendInt(status) # send status

    elif(option == 5):
        # create a thread to listen new client
        break
    elif(option == 1000000): # fix some errors of option 3
        continue






