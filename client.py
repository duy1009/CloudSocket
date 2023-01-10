from utilz.method import *
from utilz.constant import *
from utilz.Client import Client
HOST='localhost'
PORT=8000

client = Client(HOST, PORT)

# file_path = "./Data/a.py"
save_fol = "./Data_client"

while True:
    print("-----------Menu-------------")
    print("1. Get list.")
    print("2. Push file.")
    print("3. Get file.")
    print("4. Delete file.")
    print("5. Exit")
    print(">> ", end="")
    option = int(input())
    
    list_data = client.recv_data(HEADER)
    list_data = convByteToList1D(list_data,"|")

    if (option == 1):
        client.sendInt(option)
        showList(list_data)
    elif (option == 2):
        client.sendInt(option)
        
        print("Enter file path: ", end="")
        file_path = input()
        print("Enter file name: ", end="")
        file_name = input()
        # file_name = "haa.py"
        
        client.sendFileName(file_name)
        client.sendFile(file_path)
        status = client.recvInt()
        print(STATUS[status])
    elif (option == 3):
        print("Enter file sequence number: ", end="")
        snum = int(input())
        if (len(list_data) <= snum or snum < 0):
            client.sendInt(1000000)
            print("Out of length")
            continue
        else:
            client.sendInt(option)
            client.sendFileName(list_data[snum])
            status = client.recvInt()
            if (status == 2):
                f_name = list_data[snum]
                data = client.recv_data(HEADER)
                print(f"Size: {data} bytes")
                save_path = save_fol + "/" + f_name
                st = saveData(save_path, data)
                print(STATUS[st])
            elif (status == 3):
                print(STATUS[status])
    elif (option == 4):
        print("Enter file sequence number: ", end="")
        snum = int(input())
        if (len(list_data) <= snum or snum < 0):
            client.sendInt(1000000)
            print("Out of length")
            continue
        else:
            client.sendInt(option)
            client.sendFileName(list_data[snum])
            status = client.recvInt()
            if (status == 2):
                print(STATUS[st])
            elif (status == 3):
                print(STATUS[status])
    elif(option == 5):
        client.sendInt(option)
        break
    


    
