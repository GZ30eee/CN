import socket
import ssl

# Client-side function to connect to the VPN server
def vpn_client(server_ip, server_port):
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL and connect to the server
    client_socket = ssl.wrap_socket(client_socket,
                                    keyfile="client-key.pem", certfile="client-cert.pem", server_side=False,
                                    server_hostname=server_ip)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to VPN server at {server_ip}:{server_port}")

    # Send some data through the VPN tunnel
    message = "Hello from the VPN client!"
    client_socket.send(message.encode())

    # Receive the server response
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")

    # Close the connection
    client_socket.close()

# Run the VPN client
if __name__ == '__main__':
    vpn_client('127.0.0.1', 4443)
