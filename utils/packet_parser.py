# Packet Parser Stub
# Future: integrate pyshark/tshark/Zeek for flow extraction

def parse_pcap(file_path):
    print(f"[PARSER] Parsing {file_path}")
    # demo return
    return [{"src": "192.168.1.10", "dst": "8.8.8.8", "bytes": 12000}]

if __name__ == "__main__":
    flows = parse_pcap("../data/sample.pcap")
    print(flows)
