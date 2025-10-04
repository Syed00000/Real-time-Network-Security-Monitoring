import subprocess
import platform
import os

class IPBlocker:
    def __init__(self):
        self.blocked_ips = set()
        self.is_windows = platform.system() == 'Windows'
        
    def block_ip(self, ip_address):
        """Block an IP address using Windows Firewall or iptables"""
        if ip_address in self.blocked_ips:
            print(f"⚠️ {ip_address} already blocked")
            return False
        
        try:
            if self.is_windows:
                self._block_ip_windows(ip_address)
            else:
                self._block_ip_linux(ip_address)
            
            self.blocked_ips.add(ip_address)
            print(f"🚫 BLOCKED: {ip_address}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to block {ip_address}: {e}")
            return False
    
    def _block_ip_windows(self, ip_address):
        """Block IP on Windows using netsh"""
        rule_name = f"AI-NGFW_Block_{ip_address.replace('.', '_')}"
        
        # Block inbound traffic
        cmd_in = [
            'netsh', 'advfirewall', 'firewall', 'add', 'rule',
            f'name={rule_name}_IN',
            'dir=in',
            'action=block',
            f'remoteip={ip_address}'
        ]
        
        # Block outbound traffic
        cmd_out = [
            'netsh', 'advfirewall', 'firewall', 'add', 'rule',
            f'name={rule_name}_OUT',
            'dir=out',
            'action=block',
            f'remoteip={ip_address}'
        ]
        
        subprocess.run(cmd_in, check=True, capture_output=True)
        subprocess.run(cmd_out, check=True, capture_output=True)
    
    def _block_ip_linux(self, ip_address):
        """Block IP on Linux using iptables"""
        # Block INPUT
        cmd_input = ['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP']
        # Block OUTPUT
        cmd_output = ['sudo', 'iptables', '-A', 'OUTPUT', '-d', ip_address, '-j', 'DROP']
        
        subprocess.run(cmd_input, check=True, capture_output=True)
        subprocess.run(cmd_output, check=True, capture_output=True)
    
    def unblock_ip(self, ip_address):
        """Unblock an IP address"""
        if ip_address not in self.blocked_ips:
            print(f"⚠️ {ip_address} is not blocked")
            return False
        
        try:
            if self.is_windows:
                self._unblock_ip_windows(ip_address)
            else:
                self._unblock_ip_linux(ip_address)
            
            self.blocked_ips.remove(ip_address)
            print(f"✅ UNBLOCKED: {ip_address}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to unblock {ip_address}: {e}")
            return False
    
    def _unblock_ip_windows(self, ip_address):
        """Unblock IP on Windows"""
        rule_name = f"AI-NGFW_Block_{ip_address.replace('.', '_')}"
        
        cmd_in = ['netsh', 'advfirewall', 'firewall', 'delete', 'rule', f'name={rule_name}_IN']
        cmd_out = ['netsh', 'advfirewall', 'firewall', 'delete', 'rule', f'name={rule_name}_OUT']
        
        subprocess.run(cmd_in, check=True, capture_output=True)
        subprocess.run(cmd_out, check=True, capture_output=True)
    
    def _unblock_ip_linux(self, ip_address):
        """Unblock IP on Linux"""
        cmd_input = ['sudo', 'iptables', '-D', 'INPUT', '-s', ip_address, '-j', 'DROP']
        cmd_output = ['sudo', 'iptables', '-D', 'OUTPUT', '-d', ip_address, '-j', 'DROP']
        
        subprocess.run(cmd_input, check=True, capture_output=True)
        subprocess.run(cmd_output, check=True, capture_output=True)
    
    def get_blocked_ips(self):
        """Get list of blocked IPs"""
        return list(self.blocked_ips)
    
    def is_blocked(self, ip_address):
        """Check if IP is blocked"""
        return ip_address in self.blocked_ips

# Global instance
ip_blocker = IPBlocker()
