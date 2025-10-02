from scapy.all import sniff, IP, TCP, UDP, conf
import threading
import time

# Use Layer 3 socket for Windows
conf.L3socket = conf.L3socket

class PacketCapture:
    def __init__(self):
        self.total_packets = 0
        self.packet_list = []
        self.is_running = False
        
    def packet_callback(self, packet):
        """Process each captured packet"""
        self.total_packets += 1
        
        # Extract basic info
        packet_info = {
            'id': self.total_packets,
            'timestamp': time.time(),
            'size': len(packet)
        }
        
        # Get IP layer info
        if packet.haslayer(IP):
            packet_info['src_ip'] = packet[IP].src
            packet_info['dst_ip'] = packet[IP].dst
            packet_info['protocol'] = packet[IP].proto
        
        # Get port info
        if packet.haslayer(TCP):
            packet_info['src_port'] = packet[TCP].sport
            packet_info['dst_port'] = packet[TCP].dport
            packet_info['type'] = 'TCP'
        elif packet.haslayer(UDP):
            packet_info['src_port'] = packet[UDP].sport
            packet_info['dst_port'] = packet[UDP].dport
            packet_info['type'] = 'UDP'
        else:
            packet_info['type'] = 'OTHER'
        
        self.packet_list.append(packet_info)
        
        # Keep only last 100 packets
        if len(self.packet_list) > 100:
            self.packet_list.pop(0)
        
        # Print every 10 packets
        if self.total_packets % 10 == 0:
            print(f"📦 Captured {self.total_packets} packets")
    
    def start_capture(self):
        """Start capturing packets in background"""
        self.is_running = True
        
        def capture():
            print("🔍 Starting packet capture (Layer 3)...")
            try:
                # Use filter to capture only IP packets
                sniff(filter="ip", prn=self.packet_callback, store=False)
            except Exception as e:
                print(f"❌ Capture error: {e}")
        
        # Run in separate thread
        thread = threading.Thread(target=capture, daemon=True)
        thread.start()
        print("✅ Packet capture started!")
    
    def get_stats(self):
        """Return current statistics"""
        return {
            'total_packets': self.total_packets,
            'recent_packets': self.packet_list[-10:] if self.packet_list else []
        }

# Global instance
packet_capture = PacketCapture()
