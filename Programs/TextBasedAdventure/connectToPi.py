import socket               # Import socket module

def sendStep(mazeGame.validateQuestion(),c):


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
c, addr = s.accept()
print s.recv(1024)
mazeGame.runGame()
s.close                     # Close the socket when done
