import socket               # Import socket module

def sendDriveCommand(direction,methodTimeout,direction):
    if direction == 'forward':
        robotControlMethods.Forward(methodTimeout,direction)
        if robotControlMethods.Forward(methodTimeout,direction) == True:
            return True
    elif direction == 'backwards':
        robotControlMethods.Backward(methodTimeout,direction)
        if robotControlMethods.Backward(methodTimeout,direction) == True:
            return True
    elif direction == 'left':
        robotControlMethods.left(methodTimeout,direction)
        if robotControlMethods.left(methodTimeout,direction) == True:
            return True
    elif direction == 'right':
        robotControlMethods.right(methodTimeout,direction)
        if robotControlMethods.right(methodTimeout,direction) == True:
            return True

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.send('Waiting for the game to start')
   s.recv(methodTimeout,speed,direction)

c.close()                # Close the connection
