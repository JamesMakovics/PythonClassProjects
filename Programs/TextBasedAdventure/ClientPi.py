import socket
import runMotors

UDP_IP = "192.168.1.30"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    step, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    time, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    runMotors.getDriveCommand(int(step),int(time))

    if runMotors.isFinished() == True:
        sock.sendto(b"Finished")
