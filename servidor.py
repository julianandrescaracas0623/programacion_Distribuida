import socket
import threading


def handle_client(conn, addr):
    print('Conexion establecida desde {addr}')
    
    try:
        student_name = conn.recv(1024).decode()
        response  = f"Hola, {student_name} estas conectando un servidor concurrente!"
        conn.sendall(response.encode())
    except Exception as e:
        print (f"Error con {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexion cerrada con {addr}")
        
# Configuracion del servidor socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

print("Servidor escuchando en el puerto...")

while True:
    conn, addr = server.accept()
    
# creamos un thread para manejar cada cliente de forma concurrente o hilos de ejecucion para manejar cada cliente de forma concurrente
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()     
     
