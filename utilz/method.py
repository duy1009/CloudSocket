import os
def convByteToList1D(msg, char):
    return msg.decode("utf8").split(char)
def convList1DToByte(list, char):
    msg = ""
    cnt = 0
    for i in list:
        msg+= i.split("\\")[-1] 
        if cnt < len(list)-1:   
            msg+=char
        cnt+=1
    return msg.encode("utf8")
def msgWithHeader(msg, header):
    return int.to_bytes(len(msg), header,"big") + msg

def showList(list):
    if len(list) == 0:
        print("List is empty!")
    cnt = 0
    for i in list:
        print(f"({cnt}). {i}")
        cnt+=1

def saveData(path, data): #return status
    if os.path.isfile(path):
        return 1
    print(path)
    file = open(path,"wb")
    
    file.write(data)
    file.close()
    return 0

def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)