# simple network configuration validator 
# V1 --> Unauthorized port scan


import socket

ALLOWED = {22, 80, 443}

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.2)
    if s.connect_ex(('127.0.0.1', port)) == 0:
        if port not in ALLOWED:
            print(f"[ALERT] Unauthorized port {port} open")
    s.close()