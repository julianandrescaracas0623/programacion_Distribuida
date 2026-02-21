import socket
import threading
import time



contador_clientes = 0 # Variable global para contar clientes conectados
lock = threading.Lock() # Lock para sincronizar el acceso a la variable contador_clientes

def handle_client(conn, addr):
    global contador_clientes
    time.sleep(5) # Simulamos un proceso que tarda un poco en atender al cliente
    
    student_name = conn.recv(1024).decode()
    # Incrementamos el contador de clientes cada vez que se conecta un nuevo cliente
    with lock:
        contador_clientes += 1
        numero = contador_clientes
    
    print (f"Cliente conectado desde el puerto: {addr}, Total clientes conectados: {numero}")
    
    
    response = f"Hola, {student_name} estas conectando un servidor concurrente!, eres el cliente  numero: {numero}"
    conn.sendall(response.encode())
    
    conn.close()
        
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
     
