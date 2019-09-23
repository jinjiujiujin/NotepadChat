#服务端
import socket
import threading


#线程退出tag
IsRunning = True
clients = []
serverSocket = socket.socket()

#接收从客户端发送的信息
def recvMsg(clientSocket, addr):
    while IsRunning:
        client_data = clientSocket.recv(1024).decode("utf-8")
        if client_data == "quit":
            break
        msg = "{0} : {1}".format(addr[1], client_data)
        Broadcast(msg, addr)

    msg = "{0} has quit...".format(addr[1])
    print(msg)
    Broadcast(msg, addr)
    global clients
    clients.remove((clientSocket, addr))
    clientSocket.close()
    print("Current Client Number:{0}".format(len(clients)))

#向其他客户端发送
def Broadcast(msg, addr):
    for client in clients:
        if client[1] != addr:
            client[0].send(msg.encode("utf-8"))

#等待下达命令
def read():
    #如果要修改全局变量，那必须要先用global声明
    #只是引用就不需要
    global IsRunning
    while IsRunning:
        s = input("")
        if s == "quit":
            #关闭服务端
            Broadcast("CLOSE", -1)
            IsRunning = False
            global serverSocket
            serverSocket.close()
            break

def StartServer():
    #TCP协议
    global serverSocket
    #绑定本机地址和端口号
    serverSocket.bind(("127.0.0.1", 666))
    #最多5个可以连接
    serverSocket.listen(5)
    print("Server started....")

    #创建server关闭线程
    readThr = threading.Thread(target = read)
    readThr.start()

    #waiting for connection
    while IsRunning:
        client, addr = serverSocket.accept()
        clients.append((client, addr))
        print("{0} connected sucessfully".format(addr))
        print("Current Client Number:{0}".format(len(clients)))
        thr = threading.Thread(target = recvMsg, args=(client, addr))
        thr.setDaemon(True)
        thr.start()



if __name__ == "__main__":
    StartServer()