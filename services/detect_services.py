# Detection Service Stub
# Future: integrate ML models (IsolationForest, CNN, etc.)

def analyze_flow(flow):
    """
    flow: dict with src, dst, pkts, bytes, duration
    Returns: (anomaly_score, action)
    """
    # demo logic
    if flow.get("bytes", 0) > 10000:
        return 0.8, "Quarantine"
    else:
        return 0.1, "Allow"

if __name__ == "__main__":
    sample = {"src": "192.168.1.10", "dst": "8.8.8.8", "bytes": 12000}
    print(analyze_flow(sample))
