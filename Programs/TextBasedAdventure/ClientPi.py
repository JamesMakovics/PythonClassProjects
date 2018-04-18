import socket
import runMotors
import robotControlMethods

UDP_IP = "192.168.1.30"
UDP_PORT = 5005
address = UDP_IP,UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    step, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    time, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    time = int(time)
    runMotors.getDriveCommand(step,time)

    if robotControlMethods.isFinished() == True:
        sock.send(b"Finished",addr)
