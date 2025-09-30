# AI-Driven Next-Generation Firewall (Prototype)

## Problem Statement
**ID: 25160**  
**Title: AI-Driven Next-Generation Firewall for Dynamic Threat Detection and Zero Trust Implementation**

## Overview
This project is a **prototype implementation** of an intelligent firewall for SIH.  
It showcases the design of an AI-powered NGFW that integrates anomaly detection, adaptive policy enforcement, Zero Trust principles, and automation (SOAR).

⚠️ **Note:** This is a **demo prototype**. Backend detection logic and enforcement are stubs. The focus is on **architecture + UI**.

---

## Features (Demo)
- **Dashboard UI** (PyQt6)
  - Displays active flows with anomaly scores & actions
  - Buttons to allow/block traffic
- **Alerts Tab** — lists recent alerts
- **Policies Tab** — shows firewall rules
- **Logs Tab** — shows system events
- **Backend Stubs**
  - `detect_service.py`: placeholder for anomaly detection
  - `enforcer_service.py`: placeholder for policy enforcement
  - `soar_service.py`: placeholder for automation workflows
- **Modular Structure**
  - Easy to expand with real ML models, packet parsers, and federated learning

---

## Folder Structure
FireBarrier/
├─ data/ # sample datasets
├─ docs/ # diagrams, PPT
├─ models/ # ML models (future)
├─ services/ # backend service stubs
├─ ui/ # PyQt6 UI
├─ utils/ # helper scripts
├─ requirements.txt # dependencies
└─ README.md


---

## Future Scope
- **Traffic Analysis**
  - Parse PCAPs with `pyshark` or `Zeek`
  - Extract TLS/QUIC metadata and flow stats
- **AI/ML Models**
  - IsolationForest/DBSCAN for anomalies
  - CNN/LSTM for traffic patterns
  - Federated learning for distributed updates
- **Zero Trust**
  - Risk-based access control
  - Device/user verification
- **SOAR Automation**
  - Auto-block malicious IPs
  - Integration with SIEM tools
- **Performance**
  - Optimized packet processing pipelines
  - Benchmarks at enterprise scale

---

## Installation
```bash
git clone https://github.com/example/ai_ngfw_prototype
cd ai_ngfw_prototype
pip install -r requirements.txt