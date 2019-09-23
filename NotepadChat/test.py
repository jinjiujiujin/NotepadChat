import socket

if __name__ == "__main__":
    s = socket.socket()
    s.bind(("127.0.0.1", 5577))
    s.listen(2)

    while True:
        c, addr = s.accept()
        print(addr)
        print(type(addr[1]))