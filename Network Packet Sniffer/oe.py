from scapy.all import sniff, IP, TCP, UDP, ARP, conf

# Use Layer 3 socket if Npcap is not installed
conf.L3socket = conf.L3socket6  # This makes Scapy use a higher layer (Layer 3) socket

def packet_handler(packet):
    if packet.haslayer(IP):
        # Extract source and destination IP
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Check if the packet is a TCP, UDP, or ARP packet
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif packet.haslayer(ARP):
            protocol = "ARP"
            src_port = dst_port = None
        else:
            protocol = "Unknown"
            src_port = dst_port = None

        # Print packet information
        print(f"{protocol} Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

def start_sniffing():
    print("Starting packet sniffing...")
    sniff(prn=packet_handler, store=0, count=0)  # Store=0 means we do not store the packets

if __name__ == "__main__":
    start_sniffing()
