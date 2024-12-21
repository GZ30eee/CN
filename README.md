# Computer Networking Projects

This repository contains a collection of computer networking projects, showcasing various concepts and practical implementations in networking. Below is a list of the projects included:

---

### **Projects Overview**

#### **Client-Server Chat Application**
- `client.py`
- `server.py`

A simple chat application demonstrating client-server communication over TCP sockets.

#### **Dijkstra's Algorithm Graph Visualizer**
- `graph.py`

A tool for visualizing the shortest path computation using Dijkstra's algorithm.

#### **DNS Resolver**
- `dns.py`

A script to resolve domain names to IP addresses, demonstrating the working of DNS queries.

#### **HTTP Server**
- `h.py`
- `index.html`

A basic implementation of an HTTP server to serve web pages.

#### **Network Bandwidth Estimator**
- `tcp.py`

A program to estimate the bandwidth of a network connection by measuring the time taken to send a known amount of data.

#### **Network Packet Sniffer**
- `oe.py`

A packet-sniffing tool to capture and analyze network traffic at a low level.

#### **Network Traffic Monitor App**
- `net.py`

An application to monitor and display network traffic statistics.

#### **Secure Communication System Using SSL/TLS**
- `vpn_client.py`
- `vpn_server.py`
- `open.bash`

A secure client-server communication system demonstrating the use of SSL/TLS for encryption.

---

## **Getting Started**

### **Step 1: Clone the Repository**
To get started with these projects, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/GZ30eee/CN.git
cd CN
```

---

### **Step 2: Install Required Libraries**

These projects use Python and several external libraries. Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not present, manually install the following libraries:

```bash
pip install scapy networkx matplotlib
```

**Optional Libraries (depending on the project):**
- For SSL/TLS-based projects: SSL (built-in) and `pyOpenSSL`
- For Packet Sniffing: Requires elevated privileges (use `sudo` on Linux or run as Administrator on Windows).

---

## **Running the Projects**

Each project can be executed individually. Navigate to the respective directory or run the script directly, for example:

```bash
python client.py
python server.py
```

For other projects, read the inline comments or documentation in the code for specific instructions.

---

## **Contributing**
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are always welcome!

---

## **License**
This repository is open-source and available under the MIT License.
