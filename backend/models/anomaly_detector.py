# ML models (Isolation Forest, LSTM-CNN)
from sklearn.ensemble import IsolationForest
import numpy as np
import joblib
import os

class MLAnomalyDetector:
    def __init__(self):
        self.model = None
        self.is_trained = False
        self.feature_count = 0
        
    def extract_features(self, packet_info):
        """Extract numerical features from packet for ML"""
        features = []
        
        # Feature 1: Packet size
        features.append(packet_info.get('size', 0))
        
        # Feature 2: Source port (0 if not available)
        features.append(packet_info.get('src_port', 0))
        
        # Feature 3: Destination port (0 if not available)
        features.append(packet_info.get('dst_port', 0))
        
        # Feature 4: Protocol (convert to number)
        protocol_map = {'TCP': 1, 'UDP': 2, 'OTHER': 0}
        features.append(protocol_map.get(packet_info.get('type', 'OTHER'), 0))
        
        # Feature 5: IP address hash (simplified - last octet of src IP)
        src_ip = packet_info.get('src_ip', '0.0.0.0')
        try:
            last_octet = int(src_ip.split('.')[-1])
            features.append(last_octet)
        except:
            features.append(0)
        
        return features
    
    def train(self, packet_list):
        """Train Isolation Forest on normal traffic"""
        if len(packet_list) < 20:
            print("⚠️ Not enough data to train ML model (need 20+ packets)")
            return False
        
        # Extract features from all packets
        X = []
        for packet in packet_list:
            features = self.extract_features(packet)
            X.append(features)
        
        X = np.array(X)
        self.feature_count = X.shape[1]
        
        # Train Isolation Forest
        # contamination=0.1 means we expect 10% of data to be anomalies
        self.model = IsolationForest(
            contamination=0.15,  # Expect 15% anomalies
            random_state=42,
            n_estimators=100
        )
        
        print(f"🧠 Training ML model on {len(X)} packets...")
        self.model.fit(X)
        self.is_trained = True
        print("✅ ML model trained!")
        return True
    
    def predict(self, packet_info):
        """Predict if packet is anomaly (-1) or normal (1)"""
        if not self.is_trained:
            return 1  # Default to normal if not trained
        
        features = self.extract_features(packet_info)
        X = np.array([features])
        
        prediction = self.model.predict(X)[0]
        # -1 means anomaly, 1 means normal
        return prediction
    
    def is_anomaly(self, packet_info):
        """Check if packet is anomalous"""
        prediction = self.predict(packet_info)
        return prediction == -1
    
    def save_model(self, filepath='models/isolation_forest.pkl'):
        """Save trained model to disk"""
        if self.is_trained:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            joblib.dump(self.model, filepath)
            print(f"💾 Model saved to {filepath}")
    
    def load_model(self, filepath='models/isolation_forest.pkl'):
        """Load trained model from disk"""
        if os.path.exists(filepath):
            self.model = joblib.load(filepath)
            self.is_trained = True
            print(f"📂 Model loaded from {filepath}")
            return True
        return False

# Global instance
ml_detector = MLAnomalyDetector()
