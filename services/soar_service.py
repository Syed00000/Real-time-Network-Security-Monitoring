# SOAR Service Stub
# Future: automated response workflows

def handle_event(event):
    print(f"[SOAR] Handling event: {event}")
    if event["action"] == "Block":
        print("[SOAR] Triggering enforcement...")
    elif event["action"] == "Quarantine":
        print("[SOAR] Isolating host...")
    else:
        print("[SOAR] No action taken")

if __name__ == "__main__":
    test_event = {"src": "10.0.0.5", "action": "Quarantine"}
    handle_event(test_event)
