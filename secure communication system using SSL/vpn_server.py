import socket
import ssl

# Server-side function to handle incoming connections
def vpn_server(host, port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"VPN server listening on {host}:{port}...")

    # Wrap the server socket with SSL
    server_socket = ssl.wrap_socket(server_socket,
                                    keyfile="server-key.pem", certfile="server-cert.pem", server_side=True)

    while True:
        # Accept client connections
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        
        # Receive and handle data from the client
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        
        # Send a response back to the client
        response = "Data received securely"
        client_socket.send(response.encode())
        
        # Close the client socket
        client_socket.close()

# Run the VPN server
if __name__ == '__main__':
    vpn_server('127.0.0.1', 4443)
