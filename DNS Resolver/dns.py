import socket
import struct
import random

# DNS Server (Use Google Public DNS)
DNS_SERVER = "8.8.8.8"
DNS_PORT = 53

def build_query(domain):
    """
    Builds a DNS query packet.
    """
    # Header Section
    transaction_id = random.randint(0, 65535)  # Random transaction ID
    flags = 0x0100  # Standard query
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 0

    header = struct.pack('!HHHHHH', transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)

    # Question Section (Domain Name)
    qname = b''.join([bytes(chr(len(label)), 'utf-8') + bytes(label, 'utf-8') for label in domain.split('.')])
    qname += b'\0'  # Null byte to end the domain name
    qtype = 1  # A record (IPv4 address)
    qclass = 1  # IN class (Internet)
    
    question = struct.pack('!HH', qtype, qclass)
    
    # Return full DNS query packet
    return header + qname + question

def parse_response(response):
    """
    Parses the DNS response to extract the IP address.
    """
    # The header is the first 12 bytes, so skip that.
    header = response[:12]
    answer = response[12:]

    # Skip the question section (it's 2 labels + 1 byte length for each label)
    while answer[0] != 0:
        length = answer[0]
        answer = answer[1 + length:]
    
    # Skip the null byte
    answer = answer[1:]

    # We are looking for the A record, so skip QTYPE and QCLASS
    answer = answer[4:]

    # The IP address is in the answer part
    ip_address = socket.inet_ntoa(answer[:4])
    return ip_address

def dns_resolve(domain):
    """
    Resolves the domain to an IP address.
    """
    # Create UDP socket for DNS query
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    # Build the DNS query packet
    query = build_query(domain)
    
    # Send the query to the DNS server
    sock.sendto(query, (DNS_SERVER, DNS_PORT))
    
    # Receive the DNS response
    try:
        response, _ = sock.recvfrom(512)
        ip_address = parse_response(response)
        return ip_address
    except socket.timeout:
        print("DNS request timed out.")
        return None

# Test the DNS resolver
if __name__ == '__main__':
    domain = input("Enter domain name (e.g., www.google.com): ")
    ip_address = dns_resolve(domain)
    
    if ip_address:
        print(f"The IP address of {domain} is: {ip_address}")
    else:
        print("Failed to resolve the domain.")
