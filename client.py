import socket

class Client():
    def __init__(self, username):
        self.username = username
        self.host = socket.gethostname() 
        self.port = 5000

        self.client_socket = socket.socket()

    def joins_server(self):
        self.client_socket.connect((host, port))
        message = input(" -> ")  # take input

        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal

            message = input(" -> ")  # again take input

        client_socket.close()  # close the connection

