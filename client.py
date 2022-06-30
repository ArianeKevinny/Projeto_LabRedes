from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

host = str(sys.argv[1])
porta = int(sys.argv[2])
arquivo = str(sys.argv[3])
caminho = ("GET /" + arquivo + " HTTP/1.1")

try:
    clientSocket.connect((host,porta))
except Exception:
    print (Exception)
    sys.exit(0)

clientSocket.send(caminho.encode())
    
data = clientSocket.recv(1024)
    
print (data.decode() + "\r\n")
    
clientSocket.close()