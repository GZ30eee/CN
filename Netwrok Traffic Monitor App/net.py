import scapy.all as scapy
import tkinter as tk
from tkinter import messagebox
import threading
import time

class NetworkTrafficMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Monitor")
        
        self.packet_rate_label = tk.Label(root, text="Packet Rate: 0 packets/sec", font=("Helvetica", 14))
        self.packet_rate_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring, font=("Helvetica", 12))
        self.start_button.pack(pady=20)
        
        self.packet_rate = 0
        self.stop_sniffing = False
    
    def update_packet_rate(self, packet_rate):
        """Update the packet rate displayed on the GUI."""
        self.packet_rate = packet_rate
        self.packet_rate_label.config(text=f"Packet Rate: {self.packet_rate} packets/sec")
    
    def start_monitoring(self):
        """Start network monitoring in a separate thread."""
        self.stop_sniffing = False
        monitor_thread = threading.Thread(target=self.monitor_network_traffic)
        monitor_thread.start()
        
    def monitor_network_traffic(self):
        """Monitor network traffic and update packet rate in real-time."""
        scapy.sniff(prn=self.process_packet, store=0, stop_filter=self.stop_sniffing)
    
    def process_packet(self, packet):
        """Process each packet and update the packet rate."""
        # For simplicity, we count each packet and update the packet rate
        self.packet_rate += 1
        self.update_packet_rate(self.packet_rate)
        
        # Check for unusual traffic patterns (e.g., high packet rate)
        if self.packet_rate > 1000:
            messagebox.showwarning("Alert", "High traffic detected! Potential DDoS attack.")
    
    def stop_monitoring(self):
        """Stop sniffing the traffic."""
        self.stop_sniffing = True

# Set up the main window
root = tk.Tk()
app = NetworkTrafficMonitorApp(root)
root.mainloop()
