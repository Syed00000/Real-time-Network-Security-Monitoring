# Enforcer Service Stub
# Future: iptables/nftables integration

def enforce_policy(ip, action):
    print(f"[ENFORCER] {action} applied on {ip}")

if __name__ == "__main__":
    enforce_policy("192.168.1.10", "Block")
