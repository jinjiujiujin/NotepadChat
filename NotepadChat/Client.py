import socket
import threading
import time
import os


def send():
    while True:
        msg = input()
        clientSocket.send(msg.encode("utf-8"))
        if msg == "quit":
            clientSocket.close()
            #退出程序
            os._exit(0)
            
def recv():
    while True:
        try:
            msg = clientSocket.recv(1024).decode("utf-8")
            if msg == "CLOSE":
                print("SERVER: we are going to close.\n\tsee you next time...")
                #倒数3秒退出
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                clientSocket.close()
                #退出程序
                os._exit(0)
            print(msg)
        except:
            pass
        

def StartClient():
    global clientSocket
    clientSocket = socket.socket()
    clientSocket.connect(("127.0.0.1", 666))
    print("Client started...")
    #create Thread read and send 
    sendThread = threading.Thread(target=send)
    recvThread = threading.Thread(target=recv)
    sendThread.start()
    recvThread.start()
    sendThread.join()

if __name__ == "__main__":
    StartClient()
