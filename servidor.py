import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen(1)

print('Servidor esperando conexion tenga paciencia...')

conn, addr = server.accept()
print(f'Conexion establecida desde {addr}')

conn.sendall(b'Hola, Julian estas aprendiendo a programacion distribuida y has creado tu primer socket!')
conn.close()

