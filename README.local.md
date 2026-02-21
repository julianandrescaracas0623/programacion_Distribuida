# Comunicación de Sockets en Python

## Descripción General

Este proyecto implementa un ejemplo básico de **comunicación cliente-servidor** utilizando **sockets en Python**. Demuestra los conceptos fundamentales de la programación distribuida mediante la arquitectura de red TCP/IP.

---

## 📁 Estructura del Proyecto

```
├── servidor.py      # Programa que actúa como servidor
├── cliente.py       # Programa que actúa como cliente
├── hola.py          # Ejemplo básico de Python
└── README.md        # Este archivo
```

---

## 🔌 ¿Qué es un Socket?

Un **socket** es un punto final de una conexión de red. Es como un "enchufe" virtual que permite que dos programas se comuniquen a través de una red.

### Tipos de Sockets:
- **AF_INET**: Familia de direcciones IPv4
- **SOCK_STREAM**: Socket TCP (transmisión confiable de datos)

---

## 📋 Componentes del Proyecto

### 1. **Servidor (servidor.py)**

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen(1)

print('Servidor esperando conexion tenga paciencia...')

conn, addr = server.accept()
print(f'Conexion establecida desde {addr}')

conn.sendall(b'Hola, Julian estas aprendiendo a programacion distribuida y has creado tu primer socket!')
conn.close()
```

**Qué hace:**
- Crea un socket TCP
- Se vincula a la dirección IP local `127.0.0.1` en el puerto `5000`
- Escucha conexiones entrantes (máximo 1 cliente en la cola)
- Acepta la conexión del cliente
- Envía un mensaje de bienvenida
- Cierra la conexión

**Componentes clave:**
- `socket.socket()`: Crea un nuevo socket
- `bind()`: Vincula el socket a una dirección y puerto específicos
- `listen()`: Habilita el servidor para aceptar conexiones
- `accept()`: Espera y acepta una conexión entrante
- `sendall()`: Envía datos al cliente
- `close()`: Cierra la conexión

---

### 2. **Cliente (cliente.py)**

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.1", 5000))

mensaje = client.recv(1024)
print(f'Mensaje del servidor: {mensaje.decode()}')
client.close()
```

**Qué hace:**
- Crea un socket TCP
- Se conecta al servidor en `127.0.0.1` puerto `5000`
- Recibe un mensaje del servidor (máximo 1024 bytes)
- Decodifica el mensaje de bytes a texto
- Cierra la conexión

**Componentes clave:**
- `connect()`: Se conecta al servidor
- `recv()`: Recibe datos del servidor
- `decode()`: Convierte bytes a string UTF-8

---

## 🚀 Cómo Ejecutar

### Requisitos:
- Python 3.x instalado
- Sistema operativo con soporte de sockets (Linux, Windows, macOS)

### Pasos:

1. **Abre una primera terminal y ejecuta el servidor:**
   ```bash
   python3 servidor.py
   ```
   Deberías ver:
   ```
   Servidor esperando conexion tenga paciencia...
   ```

2. **Abre una segunda terminal y ejecuta el cliente:**
   ```bash
   python3 cliente.py
   ```

3. **Resultado esperado en el cliente:**
   ```
   Mensaje del servidor: Hola, Julian estas aprendiendo a programacion distribuida y has creado tu primer socket!
   ```

4. **En el servidor verás:**
   ```
   Conexion establecida desde ('127.0.0.1', puerto_asignado)
   ```

---

## 📚 Conceptos Aprendidos

### 1. **Modelo Cliente-Servidor**
La arquitectura de red más común donde:
- El **servidor** está siempre escuchando en un puerto específico
- El **cliente** inicia la conexión hacia el servidor
- Se establece un canal de comunicación bidireccional

### 2. **Protocolo TCP/IP**
- **TCP (Transmission Control Protocol)**: Garantiza que los datos se entreguen correctamente y en orden
- **Confiabilidad**: Los datos no se pierden ni se corrompen
- **Orientado a conexión**: Se establece una conexión antes de enviar datos

### 3. **Dirección IP y Puerto**
- **127.0.0.1**: Es la dirección de localhost (tu propia máquina)
- **5000**: Puerto por el que se comunican servidor y cliente
- Necesita estar disponible y no estar en uso

### 4. **Codificación de Datos**
- Los sockets transmiten datos en formato **bytes**
- Se usa `.encode()` para convertir texto a bytes
- Se usa `.decode()` para convertir bytes a texto
- Formato estándar: **UTF-8**

### 5. **Ciclo de Vida de una Conexión Socket**

```
SERVIDOR                          CLIENTE
   |                                |
   |-- Crear Socket                 |
   |-- Vincular (bind)              |
   |-- Escuchar (listen)            |
   |                                |-- Crear Socket
   |                                |-- Conectar (connect)
   |<-- Acepta (accept) --------- Conexión Establecida
   |                                |
   |-- Enviar (sendall) ----------->| Recibir (recv)
   |                                |
   |-- Cerrar (close) ------------>| Cerrar (close)
```

---

## 🔍 Detalles Técnicos Importantes

### Información de la Conexión
```python
conn, addr = server.accept()
```
- `conn`: Socket de la conexión establecida
- `addr`: Tupla con (dirección_IP, puerto_asignado_al_cliente)

### Recepción de Datos
```python
mensaje = client.recv(1024)
```
- `1024`: Tamaño máximo del buffer en bytes
- Bloquea hasta que reciba datos o se cierre la conexión

### Conversión de Datos
```python
mensaje.decode()  # bytes -> string
mensaje.encode()  # string -> bytes
```

---

## ⚠️ Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `ConnectionRefusedError` | El servidor no está corriendo | Inicia el servidor primero |
| `OSError: [Errno 48] Address already in use` | El puerto está en uso | Espera o usa otro puerto |
| `UnicodeDecodeError` | Problema al decodificar | Asegúrate de usar UTF-8 |
| `socket.timeout` | No se reciben datos a tiempo | Aumenta el timeout del socket |

---

## 🎯 Qué se Logró

✅ Crear un servidor TCP que escucha conexiones
✅ Crear un cliente TCP que se conecta a un servidor
✅ Establecer comunicación bidireccional entre procesos
✅ Comprender el flujo de datos en red
✅ Aplicar conceptos de programación distribuida

---

## 🚀 Mejoras Futuras

- Crear un servidor que acepte múltiples clientes simultáneamente (usando `threading`)
- Implementar comunicación bidireccional (cliente envía y recibe datos)
- Agregar manejo de errores más robusto
- Usar direcciones IP reales en lugar de localhost
- Implementar un protocolo de aplicación personalizado
- Agregar autenticación y encriptación

---

## 📖 Referencias

- [Documentación oficial de Python - socket](https://docs.python.org/3/library/socket.html)
- [TCP/IP Explained](https://www.geeksforgeeks.org/tcp-ip-model/)
- [Sockets de red en Python](https://realpython.com/python-sockets/)

---

**Autor:** Julian Andrés Caracas  
**Fecha:** 2026  
**Tema:** Programación Distribuida - Comunicación de Sockets en Python
