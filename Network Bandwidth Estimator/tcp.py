import socket
import time
import sys

# Function to estimate bandwidth by sending a known size of data and measuring time taken
def estimate_bandwidth(target_host, target_port, data_size=1024*1024):
    # Create a socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_host, target_port))

    # Prepare a dummy data of the specified size
    data = b'X' * data_size  # 1MB of data

    # Measure the time taken to send the data
    start_time = time.time()
    sock.sendall(data)
    sock.recv(4096)  # Receive acknowledgment (just to establish communication)
    end_time = time.time()

    # Calculate the time taken
    elapsed_time = end_time - start_time  # in seconds

    # Estimate the bandwidth (bytes per second)
    bandwidth_bps = data_size / elapsed_time  # in bytes per second
    bandwidth_mbps = bandwidth_bps / 1e6  # Convert to megabits per second

    sock.close()

    return elapsed_time, bandwidth_mbps

# Function to display results
def display_results(elapsed_time, bandwidth_mbps):
    print(f"Time taken to send data: {elapsed_time:.5f} seconds")
    print(f"Estimated Bandwidth: {bandwidth_mbps:.2f} Mbps")

def main():
    # Get target host and port
    target_host = input("Enter the target host (e.g., www.google.com): ")
    target_port = int(input("Enter the target port (e.g., 80 for HTTP): "))

    try:
        elapsed_time, bandwidth_mbps = estimate_bandwidth(target_host, target_port)
        display_results(elapsed_time, bandwidth_mbps)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
