# network_monitoring.py
import pyshark

def capture_network_traffic(interface='Wi-Fi'):
    # Function to capture network traffic from the specified interface
    packets = []
    capture = pyshark.LiveCapture(interface=interface)  # Adjust the interface as needed
    for packet in capture.sniff_continuously(packet_count=100):  # Capture 100 packets, adjust as needed
        packets.append(packet)
    return packets

def preprocess_data(packets):
    # Function to preprocess captured data and extract relevant text information
    text_data = []
    for packet in packets:
        # Extract relevant information from packet (e.g., payload, headers, etc.)
        # Convert packet data to text format
        text_data.append(str(packet))  # Example: Convert packet to string
    return text_data
