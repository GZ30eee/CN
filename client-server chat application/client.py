import socket
import threading

# Function to handle receiving messages from the server
def receive_messages(client):
    while True:
        try:
            # Receive message from the server
            message = client.recv(1024)
            if message:
                print(f"Message from server: {message.decode()}")
            else:
                break
        except:
            break

# Function to send messages to the server
def send_message(client):
    while True:
        message = input("Enter message: ")
        if message:
            client.send(message.encode())

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))  # Connect to the server on localhost, port 12345

    # Start threads to send and receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_message, args=(client,))
    
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
