from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from capture.packet_sniffer import packet_capture

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
        "total_packets": stats['total_packets'],
        "threats_detected": 0,  # We'll add this tomorrow
        "status": "running"
    }

@app.get("/api/packets")
def get_packets():
    stats = packet_capture.get_stats()
    return stats['recent_packets']

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
