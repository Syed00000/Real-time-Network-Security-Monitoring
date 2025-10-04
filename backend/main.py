from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from capture.packet_sniffer import packet_capture
from security.ip_blocker import ip_blocker  # NEW

app = FastAPI(title="AI-NGFW Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Start packet capture when app starts
@app.on_event("startup")
def startup_event():
    packet_capture.start_capture()

@app.get("/")
def read_root():
    return {"message": "AI-NGFW Backend Running!"}

@app.get("/api/stats")
def get_stats():
    stats = packet_capture.get_stats()
    return {
        "total_packets": int(stats['total_packets']),
        "threats_detected": int(stats['threats_detected']),
        "ml_threats": int(stats['ml_threats']),
        "ml_trained": bool(stats['ml_trained']),
        "blocked_ips_count": len(ip_blocker.get_blocked_ips()),  # NEW
        "status": "running"
    }

@app.get("/api/packets")
def get_packets():
    stats = packet_capture.get_stats()
    return stats['recent_packets']

@app.get("/api/threats")
def get_threats():
    """Get recent threat packets - last 10 threats"""
    threats = packet_capture.threat_list
    
    # Convert numpy types to Python native types
    clean_threats = []
    for threat in threats:
        clean_threat = {
            'id': int(threat.get('id', 0)),
            'src_ip': threat.get('src_ip', 'N/A'),
            'dst_ip': threat.get('dst_ip', 'N/A'),
            'src_port': int(threat.get('src_port', 0)) if threat.get('src_port') else None,
            'dst_port': int(threat.get('dst_port', 0)) if threat.get('dst_port') else None,
            'type': threat.get('type', 'OTHER'),
            'size': int(threat.get('size', 0)),
            'detection_method': threat.get('detection_method', 'Unknown'),
            'blocked': bool(threat.get('blocked', False)),  # NEW
            'timestamp': float(threat.get('timestamp', 0))
        }
        clean_threats.append(clean_threat)
    
    return clean_threats

# NEW: Blocked IPs endpoints
@app.get("/api/blocked-ips")
def get_blocked_ips():
    """Get list of blocked IPs"""
    return {
        "blocked_ips": ip_blocker.get_blocked_ips(),
        "count": len(ip_blocker.get_blocked_ips())
    }

@app.post("/api/block-ip/{ip_address}")
def block_ip_manual(ip_address: str):
    """Manually block an IP"""
    success = ip_blocker.block_ip(ip_address)
    return {
        "success": success,
        "ip": ip_address,
        "message": f"IP {ip_address} {'blocked' if success else 'could not be blocked'}"
    }

@app.post("/api/unblock-ip/{ip_address}")
def unblock_ip_manual(ip_address: str):
    """Manually unblock an IP"""
    success = ip_blocker.unblock_ip(ip_address)
    return {
        "success": success,
        "ip": ip_address,
        "message": f"IP {ip_address} {'unblocked' if success else 'could not be unblocked'}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
