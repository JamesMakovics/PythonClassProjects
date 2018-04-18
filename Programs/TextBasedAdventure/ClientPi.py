import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

runMotors.getDriveCommand(step,time)

if runMotors.isFinished() == True:
    sock.sendto("Finished")
