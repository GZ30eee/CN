import socket
import threading

# List to store all active client connections
clients = []

# Broadcast a message to all clients
def broadcast(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                clients.remove(c)

# Handle client communication
def handle_client(client):
    while True:
        try:
            # Receive message from the client
            message = client.recv(1024)
            if message:
                print(f"Message received: {message.decode()}")
                broadcast(message, client)
            else:
                break
        except:
            break

    # Remove the client when they disconnect
    clients.remove(client)
    client.close()

# Set up the server to listen for client connections
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))  # Listen on localhost, port 12345
    server.listen(5)
    print("Server is running and waiting for clients to connect...")

    while True:
        client, address = server.accept()
        print(f"New connection: {address}")
        clients.append(client)

        # Start a new thread to handle the client's communication
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
