## Description

## Requirements
Python 3.8

## Guide
* Install libraries
```
cd CloudSocket
pip install -r requirements.txt
```

* Run the code with multiple computers (>=2) 

We need a computer to use as a Server and other computers as Clients

Step 1: Connect 2 computers to the same wifi.

Step 2: Change the IP address in the client.py (line 5) of Clients and server.py (line 8) files of Server to the IP address of Server.

You can find the IP address with the command `ipconfig` for Windows OS or `ifconfig` for Linux.

Step 3: Run code

Server: `python server.py`

Client: `python client.py`

* Node: you can run code on a computer if you use multiple terminals instead of multiple computers and edit the ip address in step 2 is "localhost" or "127.0.0.1"

