import socket

class Server():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5000
        # initializes the server 
        self.conn = None
        self.addr = None
        self.server_socket = socket.socket()
        

    def create(self):
        self.server_socket.bind((self.host, self.port))

        # going to add  threading but for now just for 2
        self.server_socket.listen(2)
        self.conn, self.addr = self.server_socket.accept()

        print(f"Connection from ${self.addr}")

        # server running 
        while True:
            data = self.conn.recv(1024)
            
            if not data:
                break;

            print("Received from Connected User:", data)
            data = input(" -> ")
            self.conn.sendall(data.encode())

        self.conn.close()



