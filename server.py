from base64 import decode
from http import server
import socket
import threading

from network.host import getIP
from handlePage import loadPage

HOST = getIP()
PORT = 8000



socketForServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketForServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketForServer.bind((HOST, PORT))
socketForServer.listen(1)
print(f"Server is running on http://{HOST}:{PORT}")



if __name__ == "__main__":
    while True:
        clientConnecction, clientAddress = socketForServer.accept()
        
        request = clientConnecction.recv(1024).decode()
        print(request)
        
        headers = request.split('\n')
        filename = loadPage(headers[0].split()[1])
        
        response = 'HTTP/1.0 200 OK\n\n' + filename
               
        clientConnecction.sendall(response.encode())
        clientConnecction.close()
    
    socketForServer.close()