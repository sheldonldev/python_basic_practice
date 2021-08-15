import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.43.102"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    padded_send_length = send_length + b' ' * (HEADER - len(send_length))
    client.send(padded_send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))


send('hello')
input()
send('hello everyone')
input()
send('hello tim')
send(DISCONNECT_MESSAGE)

