import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (sys.argv[1], int(sys.argv[2]))
message = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00' #server title probe packet
receivedReply = False

sock.settimeout(1)
try:
    sent = sock.sendto(message, server_address)

    data, server = sock.recvfrom(4096)
    receivedReply = True
    print("Received response from " + sys.argv[1] + ":" + sys.argv[2])
except Exception as e:
    print("Did NOT receive response from " + sys.argv[1] + ":" + sys.argv[2])
finally:
    sock.close()

quit(0 if receivedReply else 1)
