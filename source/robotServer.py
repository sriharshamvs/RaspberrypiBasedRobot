import socket
from _thread import *
import sys
from hardwareControl import responseToTheRequest

## Web Socket
HOST = ''   # all available interfaces
PORT = 12345 # Non-privileged port

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Socket Created")

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print("Bind failed. Error Code: "+ str(msg[0]) + "Message : "+msg[1])
    sys.exit()

print("Socket Bind Complete")
print("PORT : "+str(PORT))

## Controls the number of incoming connections that are kept "waiting"
## if the program is already busy.
s.listen(10)
print("Socket Now Listening")

reply=b''
data=b''
dataToInt=0
response=b''

def clientThread(conn):
    conn.send(b'Welcome to the server. Type something and hit enter\n')
    while True:    
        reply=b''
        data=b''
        #now keep talking with the client
        data = conn.recv(1024)
        try :
            dataToInt = int(data)
        except ValueError:
            pass
        response = responseToTheRequest(dataToInt)
        reply = reply + response+b"\r\n\r\n"
        if not data:
            break
        response=b''
        conn.sendall(reply)
    conn.close()    
 
#now keep talking with the client
while True:
    # Wait to accept a connection - blocking call
    conn, addr = s.accept()

    # Display client information
    print("Connected with "+addr[0]+": "+str(addr[1]))

    #start new thread
    start_new_thread(clientThread,(conn,))

s.close()
