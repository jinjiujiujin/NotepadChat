import socket

if __name__ == "__main__":
    s = socket.socket()
    s.connect(("127.0.0.1", 5577))
    s.close()
