import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.1", 5000 ))

mensaje = client.recv(1024)
print(f'Mensaje del servidor: {mensaje.decode()}')
client.close()