
import os

def bloquear_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
